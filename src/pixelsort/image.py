"""image.py
All image processing functions
"""

import numpy as np
import cv2
import scipy
import logging
from functools import partial

logger = logging.getLogger(__name__)


def process_image(
    image: np.ndarray,
    create_mask: partial[np.ndarray],
    angle: float,
    sort_brightest: bool,
    reverse_sort: bool,
) -> np.ndarray:
    """
    Sorts the image in the given direction

    Args:
        image (np.ndarray): the image to sort
        angle (float): the angle to sort the image
        threshold (float): the threshold for contrast
        sort_brightest (bool): sort the brightest area of the image
        reverse_sort (bool): sort the pixels from lightest to darkest instead of darkest to lightest

    Returns:
        np.ndarray: the sorted image
    """
    logger.info(
        f"Processing image with angle={angle}, sort_brightest={sort_brightest}, reverse_sort={reverse_sort}"
    )

    logger.debug("Rotating image...")
    image_shape = np.shape(image)
    image = scipy.ndimage.rotate(image, angle, mode="reflect")

    logger.debug("Calculating areas of light and dark...")
    mask: np.ndarray = create_mask(image)
    if sort_brightest:  # invert image if we are trying to sort the brightest areas
        mask: np.ndarray = cv2.bitwise_not(mask)

    logger.debug("Sorting image...")
    for x in range(image.shape[1]):
        column_mask = mask[:, x]
        column_image = image[:, x]
        process_slice(column_mask, column_image, reverse_sort)

    logger.debug("Unrotating...")
    image = scipy.ndimage.rotate(image, -angle, mode="constant")
    new_image_shape = np.shape(image)
    image = image[
        int(new_image_shape[0] / 2 - image_shape[0] / 2) : int(
            new_image_shape[0] / 2 + image_shape[0] / 2
        ),
        int(new_image_shape[1] / 2 - image_shape[1] / 2) : int(
            new_image_shape[1] / 2 + image_shape[1] / 2
        ),
    ]

    logger.info("Done!")
    return image


def process_slice(
    mask_slice: np.ndarray, image_slice: np.ndarray, reverse: bool
) -> None:
    """process a slice of the image

    Args:
        mask_slice (np.ndarray): 1d slice of the mask mask
        image_slice (np.ndarray): 1d slice of the image
        reverse (bool): True if the pixels should be sorted in reverse
    """
    (black_pixels,) = np.where(mask_slice == 0)
    (white_pixels,) = np.where(mask_slice == 255)

    # loop through black pixels in this row
    while black_pixels.size > 0 or white_pixels.size > 0:
        # get the next black pixel
        if black_pixels.size == 0:
            x1 = mask_slice.shape[0]
        else:
            x1 = black_pixels[0]

        # remove all white pixels before the next black pixel
        white_pixels = white_pixels[white_pixels > x1]
        # get the next white pixel
        if white_pixels.size == 0:  # no more white pixels
            x2 = mask_slice.shape[0]
        else:
            x2 = white_pixels[0] - 1

        # sort pixels by luminance
        sort_pixels(image_slice[x1:x2], reverse=reverse)
        # print(x1, x2, end=" ")

        # remove all black pixels before the next white pixel
        black_pixels = black_pixels[black_pixels > x2]


def create_contrast_mask(threshold: float, image: np.ndarray) -> np.ndarray:
    """Create a contrast mask for the given image

    Args:
        image (np.ndarray): the image to create the mask for
        threshold (float): the threshold for the contrast mask

    Returns:
        np.ndarray: a contrast mask
    """
    # create contrast mask
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mean, std = cv2.meanStdDev(gray_image)
    # Calculate the lower and upper threshold values
    # Conversion of an array with ndim > 0 to a scalar is deprecated.
    # Using .item() to extract to single value.
    lower_thresh = int(mean.item() - threshold * std.item())
    upper_thresh = int(mean.item() + threshold * std.item())
    # generate mask
    mask: np.ndarray = cv2.inRange(gray_image, lower_thresh, upper_thresh)
    return mask


def create_template_mask(template: np.ndarray, image: np.ndarray) -> np.ndarray:
    """Create a mask for the given image using the template

    Args:
        image (np.ndarray): the image to create the mask for
        template (np.ndarray): the template to use for the mask

    Returns:
        np.ndarray: a contrast mask
    """
    # remove bg color channels
    template = template[:, :, 0]
    # Tile the template to the size of the image
    horizontal_tiles = int(image.shape[1] / template.shape[1]) + 1
    vertical_tiles = int(image.shape[0] / template.shape[0]) + 1
    mask = np.tile(template, (vertical_tiles, horizontal_tiles))

    # Crop the mask to the size of the image
    mask = mask[: image.shape[0], : image.shape[1]]

    return mask


def sort_pixels(image: np.ndarray, reverse: bool = False) -> None:
    """sort the pixels in the given direction by luminance

    Args:
        image (np.ndarray): the 1d array to sort
        reverse (bool): sort in reverse order
    """
    # sort pixels by luminance
    # luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
    # no point in sorting if there are less than 2 pixels
    if image.size <= 2 * 3:  # 2 pixels, 3 channels
        return

    # sort by luminance
    # numpy is b g r
    luminance = np.sum(image * [0.11, 0.59, 0.3], axis=-1)
    index = np.argsort(luminance)

    if reverse:
        index = index[::-1]

    image[:] = image[index]


def show_image(image: np.ndarray) -> None:
    cv2.imshow("image", image)
    # wait for esc
    while True:
        key = cv2.waitKey(1)
        if key == 27:
            break
    cv2.destroyAllWindows()
