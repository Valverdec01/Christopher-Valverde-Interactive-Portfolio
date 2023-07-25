import cv2
import numpy as np
import matplotlib.pyplot as plt

# Basic OpenCV Commands:

# 	1. Read image from file (imread)
# 	2. Display image in OpenCV window (imshow)
# 	3. Write image to file (imwrite)

# Get image - imread()

img = cv2.imread('watch.jpg')

if img is None:
	print("Check file path!")

# Get image info

print(type(img))

print(img.shape)

print(img.dtype)

dimensions = img.shape

height = img.shape[0]
width = img.shape [1]
channels = img.shape[2]

print('image Dimension    : ',dimensions)
print('image Height       : ',height)
print('image Width		  : ',width)
print('Number of Channels : ',channels)

# Show image - imshow()

plt.imshow(img)
plt.title('my BGR pic')
plt.show()

# Image Conversions

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title('my RGB pic')
plt.show()

# Save image - imwrite()

cv2.imwrite('watch_new.png', img)

# More image Processing!

myimg = cv2.imread('cat-grayscale.jpg')
resized = cv2.resize(myimg, (128, 128), interpolation = cv2.INTER_AREA)
mynewimg = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Get image info

print(mynewimg.shape)
print(type(mynewimg))
print(type(mynewimg.shape))

print(mynewimg[:15, :15])

# Display image - imshow()

print(mynewimg.shape)
plt.imshow(mynewimg, cmap='gray')
plt.colorbar()
plt.show()

# Save image Data - as text file

np.savetxt('mycat.csv', mynewimg, fmt='%.1f', delimiter =',')