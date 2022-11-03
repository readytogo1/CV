import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

def gasuss_noise(image,mean=0,var=0.001):
    '''
    mean 均值
    var 方差
    '''
    # 将图片转换为数组
    image = np.array(image/255,dtype=float)
    print(image)
    #  np.random.normal 从正态（高斯）分布中抽取随机样本，参数分别为正态分布中心，标准差，以及输出维度范围
    noise = np.random.normal(mean,var ** 0.5,image.shape)
    out = image+noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out,low_clip,1.0)
    out = np.uint8(out*255)
    return out

def sp_noise(image,prob):
    '''
    prob 噪声比例
    '''

    # 给定形状的用0填充的数组
    output = np.zeros(image.shape,np.uint8)
    thres = 1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j]=0 # 加入黑点
            elif rdn>thres:
                output[i][j]=255 # 加入白点
            else:
                output[i][j]=image[i][j]
    return output

img = cv2.imread('pic.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 添加椒盐噪声，比例为0.02
out1 = sp_noise(img,prob=0.02)
# 添加高斯噪声，均值为0，方差为0.009
out2 = gasuss_noise(img,mean=0,var=0.009)

cv2.imshow('original',img)
cv2.imshow('out1',out1)
cv2.imshow('out2',out2)

cv2.imwrite('sp.png',out1)
cv2.imwrite('gasuss.png',out2)

cv2.waitKey()
cv2.destroyAllWindows()