import cv2
import numpy as np
filepath="d:\py\cv\chino.png"
img_src = cv2.imread(filepath, 1)


img_bgr=cv2.split(img_src)
img_dst=cv2.merge((img_bgr[2],img_bgr[0],img_bgr[1]))


cv2.imshow("Input" , img_src)
cv2.imshow("Output", img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
