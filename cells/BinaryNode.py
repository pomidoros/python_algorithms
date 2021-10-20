from dataclasses import dataclass
from typing import Optional, TypeVar

T = TypeVar('T')


@dataclass
class BinaryNode:
    key: int
    value: T
    left: Optional["BinaryNode"] = None
    right: Optional["BinaryNode"] = None
