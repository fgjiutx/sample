import cv2
import numpy as np
import math
import sys
filepath=r"d:\py\cv\chino.png"
img_src = cv2.imread(filepath, 1)

#argm=float(sys.argv[1])

img_tmp= cv2.Laplacian(img_src, cv2.CV_32F, 3)
img_dst=cv2.convertScaleAbs(img_tmp)

cv2.imshow("Input" , img_src)
cv2.imshow("Output", img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
