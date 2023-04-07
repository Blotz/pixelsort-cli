"""image.py
All image processing functions
"""
from pixelsort.direction import Direction
import numpy as np
import cv2


def process_image(image: np.ndarray, direction: Direction, threshold: float, invert: bool, reverse_sort: bool) -> None:
    """process the given image

    Args:
        image (np.ndarray): the image to processed
        direction (Direction): the direction to sort the pixels
        threshold (float): the threshold for the contrast mask
        invert (bool): True if the selected area should be inverted
        reverse_sort (bool): True if the pixels should be sorted in reverse
    """
    is_sort_reverse = direction in [Direction.UP, Direction.LEFT]
    is_vertical = direction in [Direction.UP, Direction.DOWN]

    print(f"Processing image with {direction.name} direction, threshold={threshold}, invert={invert}, reverse_sort={reverse_sort}")

    contrast: np.ndarray = create_contrast_mask(image, threshold)
    if invert:  # invert image if sorting in reverse
        contrast: np.ndarray = cv2.bitwise_not(contrast)
    # show_image(contrast)
    # flip sort direction if sorting in reverse
    if reverse_sort:
        is_sort_reverse = not is_sort_reverse

    if is_vertical:
        for x in range(image.shape[1]):
            column_contrast = contrast[:, x]
            column_image = image[:, x]
            process_slice(column_contrast, column_image, is_sort_reverse)
    else:
        for y in range(image.shape[0]):
            row_contrast = contrast[y, :]
            row_image = image[y, :]
            process_slice(row_contrast, row_image, is_sort_reverse)

    print("Done")


def process_slice(contrast_slice: np.ndarray, image_slice: np.ndarray, is_sort_reverse: bool) -> None:
    """process a slice of the image

    Args:
        contrast_slice (np.ndarray): 1d slice of the contrast mask
        image_slice (np.ndarray): 1d slice of the image
        is_sort_reverse (bool): True if the pixels should be sorted in reverse
    """
    black_pixels, = np.where(contrast_slice == 0)
    white_pixels, = np.where(contrast_slice == 255)

    # loop through black pixels in this row
    while black_pixels.size > 0 or white_pixels.size > 0:
        # get the next black pixel
        if black_pixels.size == 0:
            x1 = contrast_slice.shape[0]
        else:
            x1 = black_pixels[0]

        # remove all white pixels before the next black pixel
        white_pixels = white_pixels[white_pixels > x1]
        # get the next white pixel
        if white_pixels.size == 0:  # no more white pixels
            x2 = contrast_slice.shape[0]
        else:
            x2 = white_pixels[0] - 1

        # sort pixels by luminance
        sort_pixels(image_slice[x1:x2], reverse=is_sort_reverse)
        # print(x1, x2, end=" ")

        # remove all black pixels before the next white pixel
        black_pixels = black_pixels[black_pixels > x2]


def create_contrast_mask(image: np.ndarray, threshold: float) -> np.ndarray:
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
    lower_thresh = int(mean - threshold * std)
    upper_thresh = int(mean + threshold * std)
    # generate mask
    contrast: np.ndarray = cv2.inRange(gray_image, lower_thresh, upper_thresh)
    return contrast


def sort_pixels(image: np.ndarray, reverse: bool = False) -> None:
    """sort the pixels in the given direction by luminance

    Args:
        image (np.ndarray): the 1d array to sort
        reverse (bool): sort in reverse order
    """
    # sort pixels by luminance
    # luminance = (r * 0.3) + (g * 0.59) + (b * 0.11)
    # no point in sorting if there are less than 2 pixels
    if image.size <= 2*3:  # 2 pixels, 3 channels
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
