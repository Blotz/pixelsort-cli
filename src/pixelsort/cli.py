"""cli.py
The main entry point of our application. 
Handles all tui actions. 
"""

from pixelsort import (__name__ as __package__name__, __doc__ as __package__doc__)
from pixelsort.direction import Direction
from pixelsort.image import process
from numpy import ndarray
from cv2 import imread, imwrite
import argparse
import pathlib
import sys
import filetype


def main() -> None:
    # read input from command line
    parser = argparse.ArgumentParser(prog=__package__name__, description=__package__doc__)
    parser.add_argument("image_path", type=str, help="path to image")
    parser.add_argument("direction", type=str, help="direction to sort pixels", choices=["up", "down", "left", "right"])
    # optional argument
    parser.add_argument("--threshold", type=float, help="threshold for contrast", default=1.0)
    parser.add_argument("--invert", type=bool, help="invert the selected area", default=False, required=False)
    parser.add_argument("--reverse_sorting", type=bool, help="reverse the sorting direction", default=False, required=False)
    # file output
    parser.add_argument("--output", type=str, help="path to output file", default=None, required=False)
    
    args = parser.parse_args()

    image_path = pathlib.Path(args.image_path)
    direction = Direction(args.direction)
    threshold = args.threshold
    invert = args.invert
    reversed_direction = args.reverse_sorting
    output_path = args.output

    # Parse image path
    if not valid_read_image_path(image_path):
        sys.exit(-1)

    # load image array
    image: ndarray = imread(str(image_path))

    # process image
    process(image, direction, threshold, invert, reversed_direction)

    # save image
    if output_path is None:
        return
    # Parse output path
    output_path = pathlib.Path(output_path)
    if not valid_write_image_path(output_path):
        sys.exit(-1)
    
    imwrite(str(output_path), image)




def valid_read_image_path(image_path: pathlib.Path) -> bool:
    """checks if the given path is a valid image path

    Args:
        image_path (pathlib.Path): the path to check

    Returns:
        bool: True if the path is valid, False otherwise
    """
    if (not image_path.exists()):
        print("image path invalid: File does not exist")
        return False

    if (not image_path.is_file()):
        print("image path invalid: Path does not point to File")
        return False

    if (not filetype.is_image(image_path)):
        print("image path invalid: File is not image")
        return False
    
    return True

def valid_write_image_path(image_path: pathlib.Path) -> bool:
    """checks if the given path is a valid image path

    Args:
        image_path (pathlib.Path): the path to check

    Returns:
        bool: True if the path is valid, False otherwise
    """
    # validate parent directory
    if (not image_path.parent.exists()):
        print("output path invalid: Parent directory does not exist")
        return False
    
    if (not image_path.parent.is_dir()):
        print("output path invalid: Parent directory is not a directory")
        return False

    # print warning if file already exists
    if (image_path.exists()):
        print("WARNING: output file already exists. Overwriting file")
    
    return True

if __name__=="__main__":
    main()
