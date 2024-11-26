"""cli.py
The main entry point of our application. 
Handles all tui actions. 
"""

import pathlib
import filetype
import logging

logger = logging.getLogger(__name__)


def valid_read_path(path: pathlib.Path) -> bool:
    """checks if the given path is a valid path

    Args:
        path (pathlib.Path): the path to check

    Returns:
        bool: True if the path is valid, False otherwise
    """
    if not path.exists():
        logger.error("path invalid: File does not exist")
        return False

    if not path.is_file():
        logger.error("path invalid: Path does not point to File")
        return False

    if not filetype.is_image(path):
        logger.error("path invalid: File is not image")
        return False

    return True


def valid_write_path(path: pathlib.Path) -> bool:
    """checks if the given path is a valid path

    Args:
        path (pathlib.Path): the path to check

    Returns:
        bool: True if the path is valid, False otherwise
    """
    # validate parent directory
    if not path.parent.exists():
        logger.error("output path invalid: Parent directory does not exist")
        return False

    if not path.parent.is_dir():
        logger.error("output path invalid: Parent directory is not a directory")
        return False

    if path.exists():
        logger.warning("WARNING: output file already exists. Overwriting file")

    return True
