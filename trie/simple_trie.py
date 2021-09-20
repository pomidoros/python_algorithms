from typing import Optional, Generic, List, TypeVar
from colorama import Fore, Back, Style
from time import time, sleep


T = TypeVar("T")


class SimpleTrie(Generic[T]):
    def __init__(self, value: Optional[T] = None) -> None:
        """
        Creating of the new trie's cell
        :param value: value for a new cell
        """
        self.key: Optional[str] = None
        self.value: Optional[T] = value
        self.branch_keys: List[str] = []
        self.children: List[SimpleTrie] = []

    def _check_lists_for_consistent(self) -> bool:
        """
        Check lists of branches for the node for length's equal
        :return: bool
        """
        return len(self.children) == len(self.branch_keys)

    def _check_key_for_consistent(self, new_key: str) -> bool:
        """
        Check new key for existing in the list
        :param new_key: new key
        :return: bool
        """
        try:
            result = self.branch_keys.index(new_key)
        except ValueError as exc:
            return True
        else:
            return False

    def _add_child(self, key: str, child: "SimpleTrie") -> bool:
        """
        Append new child by key to the cur object
        :param key: new key
        :param child: new child
        :return: bool (Is new child been added?)
        """
        if self._check_key_for_consistent(key):
            self.branch_keys.append(key)
            self.children.append(child)
            return True
        return False

    def _check_letter(self, letter: str) -> bool:
        """
        Check letter for ASCII association
        :param letter:
        :return: bool
        """
        if len(letter) != 1:
            raise Exception("Zhopa")
        return (ord(letter) >= ord('0')) and (ord(letter) <= ord('z'))

    def __setitem__(self, key: str, value: T) -> T:
        cell_link = self
        while len(key) != 0:
            first_letter = key[0]
            if first_letter in cell_link.branch_keys:
                item_index = cell_link.branch_keys.index(first_letter)
                cell_link = cell_link.children[item_index]
            else:
                new_cell = SimpleTrie()
                cell_link._add_child(first_letter, new_cell)
                cell_link = new_cell
            key = key[1:]
        cell_link.value = value
        return value

    def __getitem__(self, key: str) -> Optional[T]:
        cell_link = self
        while len(key) != 0:
            first_letter = key[0]
            if first_letter in cell_link.branch_keys:
                cell_index = cell_link.branch_keys.index(first_letter)
                cell_link = cell_link.children[cell_index]
                key = key[1:]
            else:
                return None
        return cell_link.value


if __name__ == '__main__':
    new_cell = SimpleTrie()
    new_cell["a"] = "1421412"
    new_cell["ab"] = 11
    print(new_cell["ab"])
    # new_cell.add_child("a", SimpleTrie())

