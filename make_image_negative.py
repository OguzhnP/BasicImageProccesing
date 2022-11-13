import cv2
from matplotlib import pyplot as plt

# Load the image
image = cv2.imread('Assets/image1.jpg')

# Invert the image using cv2.bitwise_not
negativeImage = cv2.bitwise_not(image)

plt.subplot(2,1,1),plt.imshow(image)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,1,2),plt.imshow(negativeImage)
plt.title('Negative'), plt.xticks([]), plt.yticks([])

plt.show()