import pytest
import cv2
import numpy as np

import itertools


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
angles = [0, 45, -90]
sort_brightest_options = [False, True]
reverse_sort_options = [False, True]
thresholds = [1, 0.5, -0.5]
template_angles = [0, 45, -90]
template_scales = [0.5, 1.5]

contrast_test_case = [
    {
        "angle": angle,
        "sort_brightest": sort_brightest,
        "reverse_sort": reverse_sort,
        "threshold": threshold, 
    } for angle, sort_brightest, reverse_sort, threshold in itertools.product(
        angles,
        sort_brightest_options,
        reverse_sort_options,
        thresholds
    )
]

template_test_case = [
    {
        "angle": angle,
        "sort_brightest": sort_brightest,
        "reverse_sort": reverse_sort,
        "template_angle": template_angle,
        "template_scale": template_scale
    }
    for angle, sort_brightest, reverse_sort, template_angle, template_scale in itertools.product(
        angles,
        sort_brightest_options,
        reverse_sort_options,
        template_angles,
        template_scales
    )
]

if __name__=="__main__":
    print(f"contract_test_case: {len(contrast_test_case)}")
    print(f"template_test_case: {len(template_test_case)}")
    print(contrast_test_case[:10])
    print(template_test_case[:10])