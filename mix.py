import cv2
import numpy as np
import gausob
import decol

filepath="d:\py\cv\chino.png"

img1=gausob.gausob(filepath,5,0)
img2=decol.kmeans(filepath,8,0)
img3=img1[0]+(1)
img_dst=img3+img2
#img_dst = cv2.addWeighted(img2,0.4,img3,1,0)
cv2.imshow("Result",img_dst)
cv2.imshow("1",img2)
cv2.imshow("2",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
