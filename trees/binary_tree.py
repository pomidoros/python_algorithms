from searching.breadth_first_search import *
from helpers.helpers import *
from random import normalvariate, randint


class BinaryNodeInterface(ABC):
    def __init__(self, name: str, data: Optional = None):
        """
        :param name: name of Node
        :param data: data of Node
        define two children: Left and Right
        """

        self.name: str = name

        self.data: Optional = data

        self.leftChild: Optional["BinaryNodeInterface"] = None

        self.rightChild: Optional["BinaryNodeInterface"] = None

    @abstractmethod
    def __str__(self):
        pass

    @staticmethod
    @abstractmethod
    def traverse(self, item: "BinaryNodeInterface") -> List["BinaryNodeInterface"]:
        pass

    @abstractmethod
    def add_child(self, child: "BinaryNodeInterface") -> None:
        pass


class UsualBinaryNode(BinaryNodeInterface):
    def add_child(self, child: "BinaryNodeInterface"):

        if self.leftChild is None:

            self.leftChild = child

        elif self.rightChild is None:

            self.rightChild = child

        else:
            return None

    def __str__(self):
        data = ''
        if self.data is not None:
            data = '\nData: ' + str(self.data)
        return self.name + data

    def traverse(self, item: "BinaryNodeInterface") -> List["BinaryNodeInterface"]:
        pass


class BinaryTree:
    def __init__(self, root: BinaryNodeInterface):
        self.root: BinaryNodeInterface = root

        self._lvl: Optional[int] = None

        self._length: Optional[int] = None

        self._fill()

    def _fill(self):
        """
        :return: None
        Set needle values for basic tree
        """
        self._length: int = len(self.list_of_nodes())
        i = 1
        while 2 ** (i - 1) <= self._length:
            i += 1
        self._lvl: int = i - 1

    def terminal_cells(self) -> int:
        # difference between common length and cells on completed levels
        return self.length() - (2 ** (self.levels() - 1) - 1)

    def _update(self):
        """
        :return:
        Update after anything adding
        """
        if len(bin(self._length)) < len(bin(self._length + 1)):
            self._lvl += 1
        self._length += 1

    # getters and outputs

    def __len__(self):
        return self.length()

    def length(self) -> int:
        return self._length

    def levels(self):
        return self._lvl

    @staticmethod
    def next_children(item: BinaryNodeInterface) -> Tuple[Optional[BinaryNodeInterface]]:
        list_of_children: List[Optional[BinaryNodeInterface]] = []

        if item.leftChild is not None:
            list_of_children.append(item.leftChild)

        if item.rightChild is not None:
            list_of_children.append(item.rightChild)

        return tuple(list_of_children)

    def print_tree(self):
        [print(cell, end=' ') for cell in self.list_of_nodes()]
        print('')

    def list_of_nodes(self) -> List[Optional[BinaryNodeInterface]]:
        """
        :return: Ordered list cells of the binary tree
        """
        return breadth_first_search(self.root, BinaryTree.next_children)

    def create_and_add(self, name: str, data=None):

        new_node = BinaryNodeInterface(name, data)

        self.add(new_node)

    def add(self, new_node):

        cur_node = self.root

        filter_expression = "{{:0<{}}}".format(self.levels())

        # get a binary sequence for new node
        result_chain = filter_expression.format(str(bin(len(self) + 1)))[3:]

        # traversing of the cells for new cell
        for sym in result_chain[:-1]:
            if int(sym) == 1:
                cur_node = cur_node.rightChild
            else:
                cur_node = cur_node.leftChild

        # adding
        if result_chain[-1] == '1':
            cur_node.rightChild = new_node
        else:
            cur_node.leftChild = new_node

        self._update()

    def cell_by_data(self, level: int, bias: int) -> UsualBinaryNode:
        return self.list_of_nodes()[2 ** (level - 1) + bias - 1]

    @staticmethod
    def generate_random_tree():

        root = UsualBinaryNode('A')

        # generate count of levels by normal distribution
        levels = round(normalvariate(4, 0.5))

        # generate count of a bias on last level
        cells_on_last_level = randint(0, 2 ** (levels - 1))

        all_count = 2 ** (levels - 1) - 1 + cells_on_last_level

        new_tree = BinaryTree(root)

        # traversing of names and adding cells
        for letter in range(ord('B'), ord('B') + all_count - 1):
            new_tree.add(UsualBinaryNode(chr(letter)))

        return new_tree


if __name__ == '__main__':
    node1 = UsualBinaryNode('a')
    node2 = UsualBinaryNode('b')
    node3 = UsualBinaryNode('c')
    node4 = UsualBinaryNode('d')
    node5 = UsualBinaryNode('e')
    node6 = UsualBinaryNode('f')
    node1.add_child(node2)
    node1.add_child(node3)
    node2.add_child(node4)
    node2.add_child(node5)
    node3.add_child(node6)
    tree = BinaryTree(node1)
    random_tree = BinaryTree.generate_random_tree()
    random_tree.print_tree()
