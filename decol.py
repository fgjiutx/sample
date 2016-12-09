import cv2
import numpy as np
import math
import sys


def kmeans(filename,K,bool):
    img_src = cv2.imread(filename, 1)

    Z = img_src.reshape((-1,3))

    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    ret,label,center=cv2.kmeans(Z,
    K,
    None,
    criteria,
    10,
    cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    img_dst = res.reshape((img_src.shape))
    if bool==0:
        return img_dst

    if bool==1:
        cv2.imshow("Original", img_src)
        cv2.imshow("Quantization", img_dst)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if bool==2:
        cv2.imwrite("Original.png", img_src)
        cv2.imwrite("Quantization.png", img_dst)
    if bool==3:
        cv2.imwrite("KMEANS_{0:04d}.png".format(K), img_dst)

if __name__=="__main__":
    filepath=input("> filepath?")
    N=int(input('> Num?'))
    mode = int(input('> Mode?'))
    if mode == 3:
        for i in range(N):
            kmeans(filepath,i+1,3)
    else:
            kmeans(filepath,N,mode)
