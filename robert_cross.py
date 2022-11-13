import cv2
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

robertsCrossH= np.array( [[ 0, 1 ],
							[ -1, 0 ]] )
robertsCrossV = np.array( [[1, 0 ],
							[0,-1 ]] )

image = cv2.imread('Assets/image1.jpg', 0).astype('float64')
image/=255.0

horizontal = ndimage.convolve( image, robertsCrossH )
vertical = ndimage.convolve( image, robertsCrossV )

editedImage = np.sqrt( np.square(horizontal) + np.square(vertical))
editedImage*=255


plt.subplot(2,1,1),plt.imshow(image)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,1,2),plt.imshow(editedImage)
plt.title('Prewitt'), plt.xticks([]), plt.yticks([])

plt.show()