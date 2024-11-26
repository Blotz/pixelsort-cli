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

# create template fixture
@pytest.fixture
def template() -> np.ndarray:
    # load template
    template = cv2.imread("test/test_template.png")

    if template is None:
        # error loading template
        raise Exception("Error loading template")
    
    return template

# array of test cases
contrast_test_case = [
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

template_test_case = [
    {
        "angle": 0,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 45,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 90,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 135,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 180,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 225,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 270,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 315,
        "sort_brightest": False,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "sort_brightest": True,
        "reverse_sort": False
    },
    {
        "angle": 0,
        "sort_brightest": False,
        "reverse_sort": True
    },
    {
        "angle": 0,
        "sort_brightest": True,
        "reverse_sort": True
    },
    {
        "angle": 0,
        "sort_brightest": False,
        "reverse_sort": False
    },
]
