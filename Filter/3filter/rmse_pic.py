from skimage.metrics import mean_squared_error as compare_mse
import cv2

img = cv2.imread('original.png')
imgG = cv2.imread('gasuss.png')
imgSP = cv2.imread('sp.png')
imgG2 = cv2.imread('g_Gaussion.png')
imgSP2 = cv2.imread('sp_Median.png')

mseG = compare_mse(imgG, img)
rmseG = mseG**0.5
mseG2 = compare_mse(imgG2, img)
rmseG2 = mseG2**0.5

mseSP = compare_mse(imgSP, img)
rmseSP = mseSP**0.5
mseSP2 = compare_mse(imgSP2, img)
rmseSP2 = mseSP2**0.5


print('Gaussion         RMSE:{:.3f}'.format(rmseG))
print('salt and pepper  RMSE:{:.3f}'.format(rmseSP))
print('Gaussion + Gaussion Filter       RMSE:{:.3f}'.format(rmseG2))
print('salt and pepper + Median Filter  RMSE:{:.3f}'.format(rmseSP2))
