import cv2
import numpy as np
import math
import sys
filepath=r"d:\py\cv\chino.png"
img_src = cv2.imread(filepath, 1)

argm=float(sys.argv[1])

Y = np.ones((256,1), dtype='uint8') * 0
for i in range(256):
    Y[i][0] = float(i)

img_dst=cv2.LUT(img_src,Y)
img_dst=cv2.cvtColor(img_dst, cv2.COLOR_RGB2GRAY)

cv2.imshow("Input" , img_src)
cv2.imshow("Output", img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
