import cv2
import numpy as np
import math
import sys
filepath=r"d:\py\cv\chino.png"
img_src = cv2.imread(filepath, 1)

argm=float(sys.argv[1])

k = argm
op = np.array([[-k, -k    ,-k],
               [-k, 1+8*k ,-k],
               [-k, -k    ,-k]])
img_tmp = cv2.filter2D(img_src, -1, op)
img_dst=cv2.convertScaleAbs(img_tmp)

cv2.imshow("Input" , img_src)
cv2.imshow("Sharpen", img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
