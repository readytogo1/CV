import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('PyrDown3.png')

r = cv2.pyrUp(img)

cv2.imshow("original",img)
cv2.imshow("pyrUp",r)

cv2.imwrite("PyrUp1.png",r)

cv2.waitKey()
cv2.destroyAllWindows()