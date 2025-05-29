from pixelsort import __name__ as __package__name__, __doc__ as __package__doc__
from pixelsort import image
from pixelsort import cli

import argparse
import sys
import pathlib
import cv2
import numpy as np
from functools import partial
import logging

logger = logging.getLogger(__name__)


def main() -> None:
    # read input from command line
    parser = argparse.ArgumentParser(
        prog=__package__name__, description=__package__doc__
    )
    parser.add_argument(
        "--angle", type=float, help="angle that the image is sorted. 0° is up. [0, 360]", default=90
    )
    # Either pipe file or file_path
    input_source = parser.add_mutually_exclusive_group()
    input_source.add_argument("--image_path", type=str, help="path to image", default=None)
    input_source.add_argument('stdin', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    
    # Either threshold or template_path optional
    threshold_template_group = parser.add_mutually_exclusive_group()
    threshold_template_group.add_argument(
        "--threshold",
        type=float,
        help="threshold for contrast. [-1.0, 1.0] Default: 1.0",
        default=1.0,
    )
    template_group = threshold_template_group.add_argument_group("Template Options")
    template_group.add_argument("--template_path", type=str, help="path to template image")
    template_group.add_argument("--template_scale", type=float, help="scale up and down the template", default=1.0)
    template_group.add_argument("--template_angle", type=float, help="angle of template", default=0)

    # optional arguments
    parser.add_argument(
        "--sort_brightest",
        type=bool,
        help="Sort the brightest area of the image. Default: True",
        default=True,
    )
    parser.add_argument(
        "--reverse_sorting",
        type=bool,
        help="Sorts the pixels from lightest to darkest instead of darkest to lightest. Default: False",
        default=False,
        required=False,
    )
    # file output
    parser.add_argument(
        "--output", type=str, help="path to output file", default=None, required=False
    )
    # select log level
    log_levels = parser.add_mutually_exclusive_group()
    log_levels.add_argument(
        "--verbose", action="store_true", help="print debug messages"
    )
    log_levels.add_argument("--quiet", action="store_true", help="print less messages")

    # parse logging args
    args = parser.parse_args()

    # loggging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif args.quiet:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.INFO)

    logger.debug("loading arguments")
    # get arguments
    image_path = None if args.image_path is None else pathlib.Path(args.image_path)
    image_stdin = args.stdin
    angle = args.angle
    threshold = args.threshold
    template_path = args.template_path
    template_scale = args.template_scale
    template_angle = args.template_angle
    sort_brightest = args.sort_brightest
    reversed_direction = args.reverse_sorting
    output_path = args.output
    
    # Manually check for mutual exclusive group
    if image_path is None and sys.stdin.isatty():
        parser.print_usage(sys.stderr)
        parser.error("one of the arguments --image_path [stdin] is required")
        
        sys.exit(2)

    if image_path is not None:
        logging.debug("Testing to see if the path is valid")
        # Parse image path
        if not cli.valid_read_path(image_path):
            sys.exit(-1)

        # load image array
        image_data: np.ndarray = cv2.imread(str(image_path))
    else:
        logging.debug("Reading from stdin")
        
        assert not sys.stdin.isatty()
        
        with open(0, 'rb') as f: 
            inpipe = f.read()
        array = np.frombuffer(inpipe, dtype='uint8')
        image_data = cv2.imdecode(array, 1)

    # process image
    if template_path is not None:
        template_path = pathlib.Path(template_path)
        # Parse template path
        if not cli.valid_read_path(template_path):
            sys.exit(-1)

        template = cv2.imread(str(template_path))
        template = image.scale_image(template, template_scale)
        create_mask = partial(image.create_template_mask, template, template_angle-angle)
    else:
        create_mask = partial(image.create_contrast_mask, threshold)

    image_data = image.process_image(
        image_data, create_mask, angle, sort_brightest, reversed_direction
    )

    # Write to stdout
    if output_path is None:
        sys.stdout.buffer.write(cv2.imencode(".png", image_data)[1].tobytes())
        sys.exit(0)

    # Parse output path
    output_path = pathlib.Path(output_path)
    if not cli.valid_write_path(output_path):
        sys.exit(-1)

    cv2.imwrite(str(output_path), image_data)


if __name__ == "__main__":
    main()
    sys.exit(0)
