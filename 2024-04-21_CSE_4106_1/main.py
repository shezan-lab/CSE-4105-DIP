import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("assets/pic2.jpg")

# # showing image on a new window
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # writing image into file
# cv2.imwrite("assets/pic3.png", img)

# width = img.shape[0]
# height = img.shape[1]
# channel = img.shape[0]
# print(width, height, channel)

# # Making the image Gray and White
# grayScaleImage= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("image", grayScaleImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Resizing Image
newWidth = 256
newHeight = 256
newImage = cv2.resize(img, (newWidth, newHeight))
# cv2.imshow("newImage", newImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.hist(newImage.ravel(), 256, [0,256])
histogram, bins = np.histogram(newImage.flatten(), bins=256, range=[0, 256])
plt.figure(figsize=(10,10))
plt.show(histogram, color='black')
plt.show()