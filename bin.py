import cv2
import numpy as np
import math
import sys
filepath=r"d:\py\cv\chino.png"
img_src = cv2.imread(filepath, 1)
img_src_gray = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

argm=int(sys.argv[1])
ret, img_dst=cv2.threshold(img_src, argm, 255, cv2.THRESH_BINARY)
retret, img_gray_bin=cv2.threshold(img_src_gray, argm, 255, cv2.THRESH_BINARY)

img_gray=cv2.cvtColor(img_dst, cv2.COLOR_RGB2GRAY)


cv2.imshow("Input" , img_src)
cv2.imshow("Binarization", img_dst)
cv2.imshow("Binarization+Grayscale", img_gray)
cv2.imshow("Grayscale+Binarization", img_gray_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
