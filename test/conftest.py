import pytest
import cv2
import numpy as np


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
        "angle": 0,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 45,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 90,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 135,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 180,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 225,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 270,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 315,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": 0.5,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": 0,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": -0.5,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": 1,
        "sort_brightest": True,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": True
    },
    {
        "angle": 0,
        "threshold": 1,
        "sort_brightest": True,
        "reverse_sort": True
    },
    {
        "angle": 0,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "threshold": 1,
        "sort_brightest": False,
        "reverse_sort": False
    }
]
