from trees.binary_tree import BinaryNode


class BinaryNodeTraverseInOrder(BinaryNode):
    def __init__(self, name: str, data=None):
        super(BinaryNodeTraverseInOrder, self).__init__(name, data)

    @staticmethod
    def traverse_in_order(cur_cell: "BinaryNodeTraverseInOrder"):
        if cur_cell.leftChild is not None:
            BinaryNodeTraverseInOrder.traverse_in_order(cur_cell.leftChild)


