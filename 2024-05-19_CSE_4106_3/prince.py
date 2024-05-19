import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def extract_even_odd_pixels(image_np):
    # Separate the even and odd indexed pixels
    even_pixels = []
    odd_pixels = []

    for i in range(image_np.shape[0]):
        for j in range(image_np.shape[1]):
            if (i % 2 == 0) and (j % 2 == 0):
                even_pixels.append(image_np[i, j])
            elif (i % 2 == 1) and (j % 2 == 1):
                odd_pixels.append(image_np[i, j])
                
    return np.array(even_pixels), np.array(odd_pixels)

def calculate_correlation(even_pixels, odd_pixels):
    # Flatten the pixel arrays in case they are multi-dimensional (e.g., RGB)
    even_pixels_flat = even_pixels.flatten()
    odd_pixels_flat = odd_pixels.flatten()
    
    # Calculate the correlation coefficient
    correlation = np.corrcoef(even_pixels_flat, odd_pixels_flat)[0, 1]
    
    return correlation

def main(image_path):
    # Load the image
    print(image_path)
    image = Image.open(image_path).convert('L')  # Convert to grayscale for simplicity
    image_np = np.array(image)
    
    # Extract even and odd indexed pixels
    even_pixels, odd_pixels = extract_even_odd_pixels(image_np)
    
    # Calculate the correlation between even and odd pixels
    correlation = calculate_correlation(even_pixels, odd_pixels)
    
    print(f"Correlation between even and odd pixels: {correlation}")

# Example usage
main("assets\pic2.jpg")
