import cv2
import numpy as np


def low_pass(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Generate Gaussian noise
    mean = 0
    sigma = 4
    gaussian_noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)

    # Add the Gaussian noise to the image
    image = cv2.add(image, gaussian_noise)

    # Apply a Mean Filter
    mean_filtered = cv2.blur(image, (5, 5))

    # Apply a Gaussian Blur
    gaussian_blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply a Median Filter
    median_filtered = cv2.medianBlur(image, 5)  # Kernel size of 5

    # Display the results
    cv2.imshow("Original Image", image)
    cv2.imshow("Mean Filter", mean_filtered)
    cv2.imshow("Gaussian Blur", gaussian_blurred)
    cv2.imshow("Median Filter", median_filtered)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
