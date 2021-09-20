from cells.BinaryCell import BinaryCell
from typing import Optional, Tuple
from random import shuffle


class OrderedBinaryTree:
    def __init__(self, root: BinaryCell):
        self.root: BinaryCell = root

    def add_cell(self, new_cell: BinaryCell):
        cur_cell = self.root
        if cur_cell.left_child is None and cur_cell.right_child is None:
            cur_cell.left_child = new_cell
            cur_cell.right_child = new_cell
            return
        cur_cell = cur_cell.right_child
        while True:
            if new_cell >= cur_cell:
                if cur_cell.right_child is not None:
                    cur_cell = cur_cell.right_child
                    continue
                else:
                    cur_cell.right_child = new_cell
                    return
            else:
                if cur_cell.left_child is not None:
                    cur_cell = cur_cell.left_child
                    continue
                else:
                    cur_cell.left_child = new_cell
                    return

    def remove_cell(self, seek_cell: BinaryCell) -> Optional[BinaryCell]:
        # Ищем родительский элемент для искомого
        parent_values: Tuple[Optional[BinaryCell], Optional[str]] = (None, None)
        if self.root.right_child is None:
            return None
        if self.root.right_child == seek_cell:
            return self.root
        cur_cell = self.root.right_child
        while True:
            if cur_cell < seek_cell:
                if cur_cell.right_child is not None:
                    if seek_cell == cur_cell.right_child:
                        parent_values = cur_cell, 'right'
                        break
                    else:
                        cur_cell = cur_cell.right_child
                        continue
                else:
                    return None
            else:
                if cur_cell.left_child is not None:
                    if seek_cell == cur_cell.left_child:
                        parent_values = cur_cell, 'left'
                        break
                    else:
                        cur_cell = cur_cell.left_child
                        continue
                else:
                    return None
        # Обрабатываем его
        parent_cell = parent_values[0]
        seek_child_orientation = parent_values[1]
        seek_cell = parent_values[0].left_child if seek_child_orientation == 'left' else parent_values[0].right_child
        if seek_cell.left_child is None:
            if seek_cell.right_child is None:
                parent_cell.right_child = None
            else:
                parent_cell.right_child = seek_cell.right_child
        else:
            most_depth_cell = seek_cell.left_child
            if most_depth_cell.right_child is None:
                parent_cell.left_child = most_depth_cell
                if seek_cell.right_child is not None:
                    parent_cell.left_child.right_child = seek_cell.right_child
            else:
                while most_depth_cell.right_child.right_child is not None:
                    most_depth_cell = most_depth_cell.right_child
                replacement_cell = most_depth_cell.right_child
                if replacement_cell.left_child is not None:
                    most_depth_cell.right_child = replacement_cell.left_child
                replacement_cell.left_child = seek_cell.left_child
                replacement_cell.right_child = seek_cell.right_child
                if seek_child_orientation == 'left':
                    parent_cell.left_child = replacement_cell
                else:
                    parent_cell.right_child = replacement_cell
        return seek_child_orientation

    def find_cell(self, seek_cell: BinaryCell) -> Optional[BinaryCell]:
        if self.root.left_child is None and self.root.right_child is None:
            return None
        cur_cell = self.root.right_child
        while True:
            if cur_cell is not None:
                if seek_cell == cur_cell:
                    return cur_cell
                elif seek_cell > cur_cell:
                    if cur_cell.right_child is not None:
                        cur_cell = cur_cell.right_child
                        continue
                    else:
                        return None
                else:
                    if cur_cell.left_child is not None:
                        cur_cell = cur_cell.left_child
                        continue
                    else:
                        return None

    @staticmethod
    def in_order_traversal(cell: BinaryCell):
        if cell.left_child is not None:
            OrderedBinaryTree.in_order_traversal(cell.left_child)
        print(cell)
        if cell.right_child is not None:
            OrderedBinaryTree.in_order_traversal(cell.right_child)

    @staticmethod
    def post_order_traversal(cell: BinaryCell):
        if cell.right_child is not None:
            OrderedBinaryTree.post_order_traversal(cell.right_child)
        print(cell)
        if cell.left_child is not None:
            OrderedBinaryTree.post_order_traversal(cell.left_child)


if __name__ == '__main__':
    root = BinaryCell()
    random_list = list(range(3))
    shuffle(random_list)
    tree = OrderedBinaryTree(root=root)
    for i in range(len(random_list)):
        tree.add_cell(BinaryCell(name=str(i + 1), value=random_list[i]))
    print(tree.root.right_child)
    print(tree.root.right_child.get_children_str())
    print(tree.root.right_child.right_child.get_children_str())
    #OrderedBinaryTree.post_order_traversal(tree.root)
