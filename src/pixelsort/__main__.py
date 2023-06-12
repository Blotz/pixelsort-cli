from pixelsort import (__name__ as __package__name__, __doc__ as __package__doc__)
from pixelsort import image
from pixelsort import cli

import argparse
import sys
import pathlib
import cv2
import numpy as np
import scipy


def main() -> None:
    # read input from command line
    parser = argparse.ArgumentParser(prog=__package__name__, description=__package__doc__)
    parser.add_argument("image_path", type=str, help="path to image")
    parser.add_argument("angle", type=float, help="angle that the image is sorted. 0° is up. [0, 360]")
    # optional argument
    parser.add_argument("--threshold", type=float, help="threshold for contrast. [-1.0, 1.0] Default: 1.0", default=1.0)
    parser.add_argument("--sort_brightest", type=bool, help="Sort the brightest area of the image. Default: True", default=True)
    parser.add_argument("--reverse_sorting", type=bool, help="Sorts the pixels from lightest to darkest instead of darkest to lightest. Default: False", default=False,
                        required=False)
    # file output
    parser.add_argument("--output", type=str, help="path to output file", default=None, required=False)

    args = parser.parse_args()

    image_path = pathlib.Path(args.image_path)
    angle = args.angle
    threshold = args.threshold
    sort_brightest = args.sort_brightest
    reversed_direction = args.reverse_sorting
    output_path = args.output

    # Parse image path
    if not cli.valid_read_image_path(image_path):
        sys.exit(-1)

    # load image array
    image_data: np.ndarray = cv2.imread(str(image_path))
  
    # process image
    image_data = image.process_image(image_data, angle, threshold, sort_brightest, reversed_direction)

    # save image
    if output_path is None:
        # show image if no output path is given
        return image.show_image(image_data)

    # Parse output path
    output_path = pathlib.Path(output_path)
    if not cli.valid_write_image_path(output_path):
        sys.exit(-1)

    cv2.imwrite(str(output_path), image_data)


if __name__ == "__main__":
    main()
