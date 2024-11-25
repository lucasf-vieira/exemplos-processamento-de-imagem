import cv2
import numpy as np


def morphological_operations(image_path):
    # Load the image
    image = cv2.imread(image_path, 0)  # Load as grayscale for binary operations

    # Threshold the image to binary
    _, binary_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

    # Define a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(binary_image, kernel, iterations=1)

    # Apply dilation
    dilated = cv2.dilate(binary_image, kernel, iterations=1)

    # Display the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Original Binary Image", binary_image)
    cv2.imshow("Eroded", eroded)
    cv2.imshow("Dilated", dilated)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
