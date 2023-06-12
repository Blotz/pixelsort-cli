import pytest
from conftest import test_cases
import numpy as np
import pixelsort


# create test cases from test_cases array
@pytest.mark.parametrize("test_case", test_cases)
def test_image_mask(image, test_case: dict):
    image_shape = np.shape(image)

    # call process function
    generated_image = pixelsort.image.process_image(image, test_case["angle"], test_case["threshold"], test_case["sort_brightest"], test_case["reverse_sort"])
    
    generated_image_shape = np.shape(generated_image)
    # assert correct shape
    assert (generated_image_shape == image_shape)
