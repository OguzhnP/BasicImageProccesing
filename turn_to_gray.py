import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loading the image and converting to gray scale
defaultImage = cv2.imread('Assets/image1.jpg',)
editedImage = cv2.cvtColor(defaultImage, cv2.COLOR_BGR2GRAY)


plt.subplot(1,2,1),plt.imshow(defaultImage)
plt.title('Original'), plt.xticks([]), plt.yticks([])   

plt.subplot(1,2,2),plt.imshow(editedImage)
plt.title('Gray'), plt.xticks([]), plt.yticks([])

plt.show()