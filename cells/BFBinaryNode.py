from cells.BinaryNode import BinaryNode
from typing import Optional


class BFBinaryNode(BinaryNode):
    height: int = 1
    left: Optional["BFBinaryNode"] = None
    right: Optional["BFBinaryNode"] = None