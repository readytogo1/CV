import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pic.png')

r1 = cv2.pyrDown(img)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)
r4 = cv2.pyrDown(r3)

# cv2.imshow("original",img)
# cv2.imshow('PyrDown1',r1)
# cv2.imshow('PyrDown2',r2)
# cv2.imshow('PyrDown3',r3)
# cv2.imshow('PyrDown4',r4)

cv2.imwrite('PyrDown1.png',r1)
cv2.imwrite('PyrDown2.png',r2)
cv2.imwrite('PyrDown3.png',r3)
cv2.imwrite('PyrDown4.png',r4)

cv2.waitKey()
cv2.destroyAllWindows()