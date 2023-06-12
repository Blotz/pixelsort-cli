"""cli.py
The main entry point of our application. 
Handles all tui actions. 
"""

import pathlib
import filetype
import logging

logger = logging.getLogger(__name__)


def valid_read_image_path(image_path: pathlib.Path) -> bool:
    """checks if the given path is a valid image path

    Args:
        image_path (pathlib.Path): the path to check

    Returns:
        bool: True if the path is valid, False otherwise
    """
    if not image_path.exists():
        logger.error("image path invalid: File does not exist")
        return False

    if not image_path.is_file():
        logger.error("image path invalid: Path does not point to File")
        return False

    if not filetype.is_image(image_path):
        logger.error("image path invalid: File is not image")
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
    if not image_path.parent.exists():
        logger.error("output path invalid: Parent directory does not exist")
        return False
    
    if not image_path.parent.is_dir():
        logger.error("output path invalid: Parent directory is not a directory")
        return False

    if image_path.exists():
        logger.warn("WARNING: output file already exists. Overwriting file")
    
    return True
