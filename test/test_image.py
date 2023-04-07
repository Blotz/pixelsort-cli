import pytest
from conftest import test_cases

import pixelsort


# create test cases from test_cases array
@pytest.mark.parametrize("test_case", test_cases)
def test_image_mask(image, test_case: dict):
    # call process function
    pixelsort.image.process_image(image, test_case["direction"], test_case["threshold"], test_case["invert"], test_case["reverse_sort"])
    assert True
