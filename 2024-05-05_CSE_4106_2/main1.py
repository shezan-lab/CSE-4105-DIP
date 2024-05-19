import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('assets/pic2.jpg')
# image = cv2.imread('assets/pic3.png')

# Check if the image has been loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:

    # # showing image on a new window
    # cv2.imshow("image", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Split the image into R, G, B channels
    B, G, R = cv2.split(image)

    # Calculate the correlation coefficients
    correlation_RG = np.corrcoef(R.flatten(), G.flatten())[0, 1]
    correlation_RB = np.corrcoef(R.flatten(), B.flatten())[0, 1]
    correlation_GB = np.corrcoef(G.flatten(), B.flatten())[0, 1]

    # Display the correlation coefficients
    print("Correlation between R and G:", correlation_RG)
    print("Correlation between R and B:", correlation_RB)
    print("Correlation between G and B:", correlation_GB)

    # Plot the spectral correlation
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].scatter(R.flatten(), G.flatten(), color='red', marker='.', alpha=0.5)
    axs[0].set_title('R vs G')
    axs[0].set_xlabel('R')
    axs[0].set_ylabel('G')
    axs[1].scatter(R.flatten(), B.flatten(), color='blue', marker='.', alpha=0.5)
    axs[1].set_title('R vs B')
    axs[1].set_xlabel('R')
    axs[1].set_ylabel('B')
    axs[2].scatter(G.flatten(), B.flatten(), color='green', marker='.', alpha=0.5)
    axs[2].set_title('G vs B')
    axs[2].set_xlabel('G')
    axs[2].set_ylabel('B')
    plt.tight_layout()
    plt.show()