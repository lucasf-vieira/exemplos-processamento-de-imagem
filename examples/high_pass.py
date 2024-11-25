import cv2
import numpy as np


def high_pass(image_path):
    # Load the image
    image = cv2.imread(image_path, 0)  # Load as grayscale for edge detection

    # Apply the Sobel filter
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    # Apply the Laplacian filter
    laplacian = cv2.Laplacian(image, cv2.CV_64F, delta=20)

    # Display the results
    cv2.imshow('Original Image', image)
    cv2.imshow('Sobel X', sobel_x.astype(np.uint8))
    cv2.imshow('Sobel Y', sobel_y.astype(np.uint8))
    cv2.imshow('Sobel Combined', sobel_combined.astype(np.uint8))
    cv2.imshow('Laplacian', laplacian.astype(np.uint8))

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
