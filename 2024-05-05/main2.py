from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np

# Load the images
blur_img = Image.open("assets/blur.jpg")
sharp_img = Image.open("assets/sharp.jpg")

# Convert images to grayscale
blur_gray = blur_img.convert("L")
sharp_gray = sharp_img.convert("L")

# Apply average spatial filtering to both images
blur_avg = blur_gray.filter(ImageFilter.BoxBlur(5))  # Adjust the radius as needed
sharp_avg = sharp_gray.filter(ImageFilter.BoxBlur(5))

# Convert images to numpy arrays
blur_arr = np.array(blur_avg)
sharp_arr = np.array(sharp_avg)

# Compute the difference between the filtered images
diff = np.abs(sharp_arr - blur_arr)

# Display the images and the difference
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.title('Blurred Image')
plt.imshow(blur_arr, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Sharp Image')
plt.imshow(sharp_arr, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Difference')
plt.imshow(diff, cmap='gray')
plt.axis('off')

plt.show()
