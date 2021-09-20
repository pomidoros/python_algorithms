from typing import Optional, Generic, TypeVar

T = TypeVar('T')


class BinaryCell(Generic[T]):
    def __init__(self, name: str = "root", value: Optional[T] = None):
        self.name: str = name
        self.value: T = value
        self.left_child: Optional[BinaryCell] = None
        self.right_child: Optional[BinaryCell] = None

    def __str__(self):
        return "Node {name}: {value}".format(name=self.name, value=self.value)

    def get_children_str(self):
        return "Children:\n" + self.left_child.__str__() + self.right_child.__str__()

    def __eq__(self, other: "BinaryCell"):
        return self.value == other.value

    def __lt__(self, other: "BinaryCell"):
        return self.value < other.value

    def __le__(self, other: "BinaryCell"):
        return self.value <= other.value

    def __gt__(self, other: "BinaryCell"):
        return self.value > other.value

    def __ge__(self, other: "BinaryCell"):
        return self.value >= other.value