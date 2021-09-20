from trees.binary_tree import BinaryNodeInterface
from helpers.helpers import *


class BinaryNodeStraightTraverse(BinaryNodeInterface):
    def __init__(self, name: str, data=None):
        super(BinaryNodeStraightTraverse, self).__init__(name, data)

    def traverse(self) -> List["BinaryNodeInterface"]:
        list_of_values = list()
        list_of_values.append(self)
        list_of_values.extend(self.leftChild.traverse())
        list_of_values.extend(self.rightChild.traverse())
        return list_of_values


class BinaryNodeSymmetricTraverse(BinaryNodeInterface):
    def __init__(self, name: str, data=None):
        super(BinaryNodeSymmetricTraverse, self).__init__(name, data)

    def traverse(self) -> List["BinaryNodeInterface"]:
        list_of_values = list()
        if self.leftChild is not None:
            list_of_values.extend(self.leftChild.traverse())
        list_of_values.append(self)
        if self.rightChild is not None:
            list_of_values.extend(self.rightChild.traverse())
        return list_of_values


class BinaryNodeReverseOrderTraverse(BinaryNodeInterface):
    def __init__(self, name: str, data=None):
        super(BinaryNodeReverseOrderTraverse, self).__init__(name, data)

    def traverse(self) -> List["BinaryNodeInterface"]:
        list_of_values = list()
        list_of_values.extend(self.rightChild.traverse())
        list_of_values.append(self)
        list_of_values.extend(self.leftChild.traverse())
        return list_of_values


