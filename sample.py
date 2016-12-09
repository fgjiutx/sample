import cv2
filename="d:\py\cv\chino.png"
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Chino chan KAWAIIII!!!!!!!!", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
