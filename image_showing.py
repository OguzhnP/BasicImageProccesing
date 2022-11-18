import cv2
import numpy as np

image=cv2.imread("Assets/image1.jpg")

cv2.imshow("Bear",image)

cv2.waitKey(0)
cv2.destroyAllWindows()