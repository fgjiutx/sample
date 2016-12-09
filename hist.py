import cv2
import numpy as np
import sys
filepath="d:\py\cv\chino.png"
img_src = cv2.imread(filepath, 1)

argm=sys.argv[1]
gamma=float(argm)

Y = np.ones((256,1), dtype='uint8') * 0
for i in range(256):
    Y[i][0] = 255* pow(float(i) / 255 , 1.0 / gamma)

img_dst=cv2.LUT(img_src,Y)

images = [img_src, img_dst]

    rows[i], cols[i] = img_hist[i].shape
    hdims[i]= [256]
    hranges[i]=[0,256]
    hist[i]= cv2.calcHist([images[i]], [0], None, hdims[i], hranges[i])
    man_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(hist[i])

    for j in range(0,255):
        v = hist[i]
        cv2.line(img_dst, (j,rows), (j, rows - rows * (v / max_val)), (255,255,255))

cv2.imshow("Input" , img_src)
cv2.imshow("Output", img_dst)
cv2.imshow("Histgram(Input)",  img_hist[0])
cv2.imshow("Histgram(Output)", img_hist[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
