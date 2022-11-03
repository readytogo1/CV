import cv2
import numpy as np
import matplotlib.pyplot as plt

img_g = cv2.imread("gasuss.png")
img_sp = cv2.imread("sp.png")

# 高斯滤波
img_g_Gaussion = cv2.GaussianBlur(img_g,(5,5),0)
img_sp_Gaussion = cv2.GaussianBlur(img_sp,(5,5),0)

# 中值滤波
img_g_Median = cv2.medianBlur(img_g,5)
img_sp_Median = cv2.medianBlur(img_sp,5)

cv2.imwrite('g_Gaussion.png',img_g_Gaussion)
cv2.imwrite('sp_Gaussion.png',img_sp_Gaussion)
cv2.imwrite('g_Median.png',img_g_Median)
cv2.imwrite('sp_Median.png',img_sp_Median)

cv2.waitKey()
cv2.destroyAllWindows()