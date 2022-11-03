import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 读取图像
img = cv2.imread('picture\small.png')
lenna_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel算子
x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)  # 对x求一阶导，垂直检测
y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)  # 对y求一阶导，水平检测

# 实现将原图片转换为uint8类型
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
#print(absX)
Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)



sns.set()
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示，必须放在sns.set之后
np.random.seed(0)
uniform_data = np.random.rand(10, 12) #设置二维矩阵
f, ax = plt.subplots(figsize=(9, 6))

#heatmap后第一个参数是显示值,vmin和vmax可设置右侧刻度条的范围,
#参数annot=True表示在对应模块中注释值
# 参数linewidths是控制网格间间隔
#参数cbar是否显示右侧颜色条，默认显示，设置为None时不显示
#参数cmap可调控热图颜色，具体颜色种类参考：https://blog.csdn.net/ztf312/article/details/102474190
sns.heatmap(Sobel, ax=ax,vmin=0,vmax=120,cmap='YlGnBu',annot=False,linewidths=0.5,cbar=True)

ax.set_title('amplitude') #设置图片标题
plt.show()


