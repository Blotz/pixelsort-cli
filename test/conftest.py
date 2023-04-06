import pytest
import cv2
import numpy as np
from pixelsorter import direction

# create image fixture
@pytest.fixture
def image() -> np.ndarray:
    # load image
    image = cv2.imread("test/test_image.jpg")

    if image is None:
        # error loading image
        raise Exception("Error loading image")
    
    return image

# array of test cases
test_cases = [
    {
        "direction": direction.Direction.UP,
        "threshold": 0.5,
        "invert": False,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.DOWN,
        "threshold": 0.5,
        "invert": False,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.LEFT,
        "threshold": 0.5,
        "invert": False,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.RIGHT,
        "threshold": 0.5,
        "invert": False,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.RIGHT,
        "threshold": 0.0,
        "invert": False,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.RIGHT,
        "threshold": 1.0,
        "invert": False,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.RIGHT,
        "threshold": 0.5,
        "invert": True,
        "reverse_sort": False
    },
    {
        "direction": direction.Direction.RIGHT,
        "threshold": 0.5,
        "invert": False,
        "reverse_sort": True
    },
    {
        "direction": direction.Direction.RIGHT,
        "threshold": 0.5,
        "invert": True,
        "reverse_sort": True
    }
]
