from helpers.helpers import *
from random import randint, randrange
from math import sqrt, floor
from numerical_algorithms.primary_numbers import PrimaryNumbers
from numerical_algorithms.exponentiation import Exponentiation


T = TypeVar('T')


class HashTable(ABC, Generic[T]):
    def __init__(self, count: int, type_table: str = 'int'):
        self.probe_object: Probe = self.create_probe(count)
        self._set_hash(type_table)
        self.main_array: List[Optional[T]] = [None] * self.probe_object.get_length()

    def _set_hash(self, type_table: str):
        hash_func = None
        if type_table == "int":
            hash_func = lambda obj, value: value % obj.probe_object.get_length()
        elif type_table == "str":
            pass
        setattr(self.__class__, "hash", hash_func)

    @abstractmethod
    def create_probe(self, count: int) -> "Probe":
        pass

    def find(self, item: T) -> Optional[Tuple[T, int]]:
        i = 1
        cur_hash = self.probe_object.probe(self.hash(item), i)
        while self.main_array[cur_hash] is not None and i != self.probe_object.get_length():
            if self.main_array[cur_hash] == item:
                return item, i
            i += 1
            cur_hash = self.probe_object.probe(self.hash(item), i)
        return None

    def delete(self, item: T) -> Optional[Tuple[T, int]]:
        i = 1
        cur_hash: int = self.probe_object.probe(self.hash(item), i)
        while self.main_array[cur_hash] is not None and i != self.probe_object.get_length():
            if self.main_array[cur_hash] == item:
                self.main_array[cur_hash] = float('-inf')
                return item, i
            i += 1
            cur_hash: int = self.probe_object.probe(self.hash(item), i)
        return None

    def insert(self, item: T) -> Optional[Tuple[T, int]]:
        i = 1
        cur_hash: int = self.probe_object.probe(self.hash(item), i)
        while self.main_array[cur_hash] is not None and i != self.probe_object.get_length():
            i += 1
            cur_hash: int = self.probe_object.probe(self.hash(item), i)
        if i == self.probe_object.get_length():
            return None
        elif self.main_array[cur_hash] is None:
            self.main_array[cur_hash] = item
            return item, i

    def __str__(self) -> str:
        return str(self.main_array)

    def __repr__(self) -> str:
        return repr(self.main_array)

    def __len__(self) -> int:
        return self.probe_object.get_length()


class LinearHashTable(HashTable):
    def __init__(self, count: int, type_table: str = "int"):
        super(LinearHashTable, self).__init__(count, type_table)

    def create_probe(self, count: int) -> "LinearProbe":
        return LinearProbeA(count)

    def get_step(self) -> int:
        return self.probe_object.get_step()


class QuadraticHashTable(HashTable):
    def __init__(self, count: int, type_table: str = "int"):
        super(QuadraticHashTable, self).__init__(count, type_table)

    def create_probe(self, count: int) -> "QuadraticProbe":
        return QuadraticProbe(count)


class Probe(ABC, Generic[T]):
    def __init__(self, count: int):
        self._alpha: float = 0.75
        self._count: int = int(1/self._alpha * count)
        self._length: int = self.set_length()

    @abstractmethod
    def set_length(self) -> int:
        pass

    @abstractmethod
    def probe(self, hash_value: int, i: int) -> int:
        pass

    def get_length(self) -> int:
        return self._length


class LinearProbe(Probe, ABC):
    def __init__(self, count: int):
        super(LinearProbe, self).__init__(count)
        self.__step: int = self._generate_step()

    @abstractmethod
    def _generate_step(self) -> int:
        pass

    @abstractmethod
    def set_length(self) -> int:
        pass

    def probe(self, hash_value: int, i: int) -> int:
        return (hash_value + (i - 1) * self.__step) % self.get_length()

    def get_step(self) -> int:
        return self.__step


class LinearProbeA(LinearProbe):
    def __init__(self, count: int):
        super(LinearProbeA, self).__init__(count)

    def _generate_step(self) -> int:
        return randrange(1, self._length, 2)

    def set_length(self):
        return Exponentiation.minimum_degree_upper_number(self._count)


class LinearProbeB(LinearProbe):
    def __init__(self, count: int):
        super(LinearProbeB, self).__init__(count)

    def _generate_step(self):
        return randint(1, self._length)

    def set_length(self):
        return PrimaryNumbers.minimum_prime_upper_number(self._count)


class QuadraticProbe(Probe):
    def __init__(self, count: int):
        super(QuadraticProbe, self).__init__(count)

    def set_length(self) -> int:
        return Exponentiation.minimum_degree_upper_number(self._count)

    @staticmethod
    def _step_params() -> Dict[str, float]:
        return {
            'c1': 0.5,
            'c2': 0.5
        }

    def probe(self, hash_value: int, i: int) -> int:
        return int(hash_value + QuadraticProbe._step_params()['c1'] * (i - 1) + QuadraticProbe._step_params()['c2'] * pow(i - 1, 2)) % self.get_length()


if __name__ == '__main__':
    obj = QuadraticHashTable(10)
    obj.insert(16)
    print(obj)