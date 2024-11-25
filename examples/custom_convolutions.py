import cv2
import numpy as np


def custom_convolutions(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Define a custom kernel for sharpening
    sharpen_kernel = np.array([[0, -1,  0],
                               [-1, 5, -1],
                               [0, -1,  0]], dtype=np.float32)

    # Define a custom kernel for edge enhancement
    edge_kernel = np.array([[-1, -1, -1],
                            [-1,  8, -1],
                            [-1, -1, -1]], dtype=np.float32)

    # Apply the custom sharpening kernel
    sharpened = cv2.filter2D(image, -1, sharpen_kernel)

    # Apply the custom edge enhancement kernel
    edges_enhanced = cv2.filter2D(image, -1, edge_kernel)

    # Display the results
    cv2.imshow('Original Image', image)
    cv2.imshow('Sharpened Image', sharpened)
    cv2.imshow('Edge Enhanced Image', edges_enhanced)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
