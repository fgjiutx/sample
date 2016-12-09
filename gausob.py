import cv2
import numpy as np
import math
import sys

def gausob(filename,sdiv,bool):
    img_src = cv2.imread(filename, 1)

    img_gau= cv2.GaussianBlur(img_src,(11,11), sdiv)
    img_tmp= cv2.Sobel(img_gau, cv2.CV_32F, 1, 0)
    img_dst=cv2.convertScaleAbs(img_tmp)
    img_dst_gray=cv2.cvtColor(img_dst, cv2.COLOR_RGB2GRAY)
    if bool==1:
        cv2.imshow("Input" , img_src)
        cv2.imshow("Sobel+Gaussian", img_dst)
        cv2.imshow("Gaussian" , img_gau)
        cv2.imshow("Sobel+Gaussian+Grayscale", img_dst_gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    if bool==2:
        cv2.imwrite("Input.png" , img_src)
        cv2.imwrite("Sobel+Gaussian.png", img_dst)
        cv2.imwrite("Gaussian.png" , img_gau)
        cv2.imwrite("Sobel+Gaussian+Grayscale.png", img_dst_gray)
    img_dst = res.reshape((img_src.shape))
    return [img_dst_gray,img_dst,img_gau]

if __name__=="__main__":
    filepath=r"d:\py\cv\chino.png"
    gausob(filepath,5,1)
