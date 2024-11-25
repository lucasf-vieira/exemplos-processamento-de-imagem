import sys

from examples.custom_convolutions import custom_convolutions
from examples.high_pass import high_pass
from examples.low_pass import low_pass
from examples.morphological_operations import morphological_operations

if __name__ == "__main__":
    image_path = (
        "dataset/Classic/airplane.bmp"
    )

    if len(sys.argv) > 1:
        filter_type = sys.argv[1]
    else:
        print("Usage: python run.py <filter_type>")
        print("Available filters: low_p, high_p, morph, custom")
        sys.exit(1)

    if filter_type == "low_p":
        low_pass(image_path)
    elif filter_type == "high_p":
        high_pass(image_path)
    elif filter_type == "morph":
        morphological_operations(image_path)
    elif filter_type == "custom":
        custom_convolutions(image_path)
    else:
        print("Invalid filter type")
        print("Available filters: low_p, high_p, morph, custom")
        sys.exit(1)
