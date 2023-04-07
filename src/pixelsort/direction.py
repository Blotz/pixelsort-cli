"""direction.py
Simple direction enum for use in the main workflow.
Allows for easy direction specification.
"""

from enum import Enum


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
