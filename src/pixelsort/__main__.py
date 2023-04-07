from pixelsort import (__name__ as __package__name__, __doc__ as __package__doc__)
from pixelsort import direction as search_direction
from pixelsort import image
from pixelsort import cli

import argparse
import sys
import pathlib
import cv2
import numpy as np


def main() -> None:
    # read input from command line
    parser = argparse.ArgumentParser(prog=__package__name__, description=__package__doc__)
    parser.add_argument("image_path", type=str, help="path to image")
    parser.add_argument("direction", type=str, help="direction to sort pixels", choices=["up", "down", "left", "right"])
    # optional argument
    parser.add_argument("--threshold", type=float, help="threshold for contrast", default=1.0)
    parser.add_argument("--invert", type=bool, help="invert the selected area", default=False, required=False)
    parser.add_argument("--reverse_sorting", type=bool, help="reverse the sorting direction", default=False,
                        required=False)
    # file output
    parser.add_argument("--output", type=str, help="path to output file", default=None, required=False)

    args = parser.parse_args()

    image_path = pathlib.Path(args.image_path)
    direction = search_direction.Direction(args.direction)
    threshold = args.threshold
    invert = args.invert
    reversed_direction = args.reverse_sorting
    output_path = args.output

    # Parse image path
    if not cli.valid_read_image_path(image_path):
        sys.exit(-1)

    # load image array
    image_data: np.ndarray = cv2.imread(str(image_path))

    # process image
    image.process_image(image_data, direction, threshold, invert, reversed_direction)

    # save image
    if output_path is None:
        # show image if no output path is given
        image.show_image(image_data)

    # Parse output path
    output_path = pathlib.Path(output_path)
    if not cli.valid_write_image_path(output_path):
        sys.exit(-1)

    cv2.imwrite(str(output_path), image_data)


if __name__ == "__main__":
    main()
