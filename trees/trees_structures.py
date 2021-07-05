from helpers.helpers import *


class BinaryNode(object):
    def __init__(self, name: str, data=None):
        self.name: str = name
        self.leftChild: Optional[BinaryNode] = None
        self.rightChild: Optional[BinaryNode] = None
        self.data: Optional = data


class Node(object):
    def __init__(self, name: str, data=None):
        self.name = name
        self.children: Optional[List[Node]] = []
        self.data: Optional = data


class Branch(object):
    def __init__(self, data=None):
        self.childNode: Optional[Node] = None
        self.data: Optional = data


class NodeInfo(object):
    def __init__(self, name: str, data=None):
        self.name: str = name
        self.children: Optional[List[NodeInfo]] = []
        self.childenData: Optional[List] = []
        self.data: Optional = data


class BinaryTree:
    def __init__(self, root: BinaryNode):
        self.root: BinaryNode = root

    @staticmethod
    def add_left_child(for_node: BinaryNode, child: BinaryNode):
        for_node.leftChild = child

    @staticmethod
    def add_right_child(for_node: BinaryNode, child: BinaryNode):
        for_node.rightChild = child


if __name__ == '__main__':
    root = BinaryNode('A')
    tree = BinaryTree(root)
    nodeB = BinaryNode('B')
    nodeC = BinaryNode('C')
    nodeD = BinaryNode('D')
    nodeE = BinaryNode('E')
    BinaryTree.add_left_child(root, nodeB)
    BinaryTree.add_right_child(root, nodeC)
    BinaryTree.add_left_child(nodeB, nodeD)
    BinaryTree.add_right_child(nodeB, nodeE)
