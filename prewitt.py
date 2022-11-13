import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Assets/image1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaussianImage = cv2.GaussianBlur(gray,(3,3),0)


# Prewitt Filtering
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
xPrewittImage = cv2.filter2D(gaussianImage, -1, kernelx)
yPrewittImage = cv2.filter2D(gaussianImage, -1, kernely)



plt.subplot(2,2,1),plt.imshow(image)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(xPrewittImage + yPrewittImage)
plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(xPrewittImage)
plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(yPrewittImage)
plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])

plt.show()