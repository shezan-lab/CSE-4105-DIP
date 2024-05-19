import cv2
import numpy as np

# Load the image
image_path = "assets\pic2.jpg"
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get dimensions of the image
height, width = gray_image.shape

# Initialize arrays to store odd and even pixel values
odd_pixels = np.zeros((height, width), dtype=np.uint8)
even_pixels = np.zeros((height, width), dtype=np.uint8)

# Iterate through each pixel
for i in range(height):
    for j in range(width):
        # If both row and column indices are odd, store the pixel value in odd_pixels
        if i % 2 != 0 and j % 2 != 0:
            odd_pixels[i, j] = gray_image[i, j]
        # If both row and column indices are even, store the pixel value in even_pixels
        elif i % 2 == 0 and j % 2 == 0:
            even_pixels[i, j] = gray_image[i, j]

# Calculate the correlation between odd and even pixels
correlation = np.corrcoef(odd_pixels.flatten(), even_pixels.flatten())[0, 1]

print("Correlation between odd and even pixels:", correlation)

# Display the images constructed from odd and even pixels
cv2.imshow("Odd Pixels Image", odd_pixels)
cv2.imshow("Even Pixels Image", even_pixels)
cv2.waitKey(0)
cv2.destroyAllWindows()
