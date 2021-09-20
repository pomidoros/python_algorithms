from typing import Optional, Generic, TypeVar, List

T = TypeVar("T")


class CompressedTrie(Generic[T]):
    def __init__(self, key=Optional[str], child=Optional["CompressedTrie"],
                 brother=Optional["CompressedTrie"], value=Optional[T]):
        self.value: Optional[T] = value
        self.key: Optional[str] = key
        self.brother: Optional[CompressedTrie] = brother
        self.child: Optional[CompressedTrie] = child


class CompressTrieWorking(Generic[T]):
    @classmethod
    def prefix_length(cls, key: str, required_key: str):
        for i in range(len(required_key)):
            if key[i] == required_key[i]:
                continue
            return i

    @classmethod
    def find(cls, cell: "CompressedTrie", key: str):
        if cell is None:
            return None
        prefix_length = cls.prefix_length(cell.key, key)
        if prefix_length == 0:
            return cls.find(cell.brother, key[prefix_length:])
        if prefix_length < len(key):
            return cls.find(cell.child, key[prefix_length:])
        if prefix_length == len(key):
            return cell.value

    @classmethod
    def insert(cls, cell: "CompressedTrie", key: str, value: T) -> Optional[CompressedTrie]:


    @classmethod
    def split(cls, cell: "CompressedTrie", split_length: int):
        second_part = cell.key[split_length:]
        new_cell = CompressedTrie(key=second_part, child=cell.child)
        cell.child = new_cell
        cell.key = cell.key[:split_length]

    @classmethod
    def delete(cls, cell: "CompressedTrie", key: str):
        pass
