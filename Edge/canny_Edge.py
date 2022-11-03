import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv2.imread('picture\pic.png')
lenna_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#灰度化处理
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#高斯滤波降噪
gaussian = cv2.GaussianBlur(grayImage, (3, 3), 0)

#腐蚀化
kernel = np.ones((5,5), np.uint8)
k_ys = cv2.morphologyEx(gaussian, cv2.MORPH_OPEN, kernel)

#Canny算子
Canny = cv2.Canny(k_ys, 50, 150)

#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

#显示图形
titles = [u'原始图像', u'高斯滤波',u'Canny算子',]
images = [lenna_img, k_ys,Canny,]
for i in range(3):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('canny.png',Canny)