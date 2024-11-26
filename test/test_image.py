import pytest
from conftest import contrast_test_case, template_test_case
import numpy as np
from functools import partial
import pixelsort


@pytest.mark.parametrize("test_case", contrast_test_case)
def test_image_contrast_mask(image, test_case: dict):
    image_shape = np.shape(image)

    # call process function
    create_mask = partial(pixelsort.image.create_contrast_mask, test_case["threshold"])
    generated_image = pixelsort.image.process_image(image, create_mask, test_case["angle"], test_case["sort_brightest"], test_case["reverse_sort"])
    
    generated_image_shape = np.shape(generated_image)
    # assert correct shape
    assert (generated_image_shape == image_shape)


@pytest.mark.parametrize("test_case", template_test_case)
def test_image_template_mask(image, template, test_case: dict):
    image_shape = np.shape(image)

    # call process function
    create_mask = partial(pixelsort.image.create_template_mask, template)
    generated_image = pixelsort.image.process_image(image, create_mask, test_case["angle"], test_case["sort_brightest"], test_case["reverse_sort"])
    
    generated_image_shape = np.shape(generated_image)
    # assert correct shape
    assert (generated_image_shape == image_shape)