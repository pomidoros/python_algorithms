from stacks_and_deques.stack_algorithms.stack import ArrayStack
from typing import TypeVar, Generic

T = TypeVar('T')


class SortedStacks(Generic[T], ArrayStack):
    def __init__(self):
        super().__init__()

    def get_last_item(self) -> T:
        """
    :return: возвращает последний элемент из массива, не удаляя его
        """
        return self._array[self.next_index - 1]

    def insert_sort_decreasing(self) -> None:
        """
    сортирует массив в обратном порядке посредством сортировки вставки
        """
        # создаём вспомогательный стек
        intermediate_stack: ArrayStack = ArrayStack(self.count)
        # по очереди получаем все индексы для их обработки
        for i in range(self.next_index):
            # сохраняем последний элемент из стека
            finite: T = self.pop()
            # переправляем все неотсортированные данные во вспомогательный стек
            for j in range(self.next_index - i - 1):
                intermediate_stack.push(self.pop())
            # когда мы добрались до отсортированной части - вставляем в неё сохранённый элемент в порядке возврастания
            while (self.next_index != 0) and (self.get_last_item() < finite):
                intermediate_stack.push(self.pop())
            intermediate_stack.push(finite)
            # перекачиваем весь вспомогательный стек обратно в основной
            while intermediate_stack.next_index != 0:
                self.push(intermediate_stack.pop())

    def insert_sort_ascending(self) -> None:
        """
    :return: сортирует по возврастанию посредством сортировки вставки
        """
        # создаём вспомогательный стек
        intermediate_stack = ArrayStack(self.count)
        # обрабатываем каждый элемент из него
        for i in range(self.next_index):
            # сохраняем последний элемент из него
            finite: T = self.pop()
            # переправляем все неотсортированные элементы из основного стека во вспомогательный
            for j in range(self.next_index - 1 - i):
                intermediate_stack.push(self.pop())
            # вставляем в отсортированную часть выбранный элемент в порядке убывания
            while (self.next_index != 0) and (finite < self.get_last_item()):
                intermediate_stack.push(self.pop())
            self.push(finite)
            # переводим весь вспомогательный стек назад в основной
            while intermediate_stack.next_index != 0:
                self.push(intermediate_stack.pop())

    def cut(self) -> None:
        """
    Обрезает пустые значения в массиве
        """
        self._array = self._array[:self.next_index]

    def select_sort_decreasing(self) -> None:
        """
    :return: сортирует в обратном порядке поредством сортировки выбора
        """
        intermediate_stack = ArrayStack(self.count)
        for i in range(self.next_index):
            largest = self.get_last_item()
            for j in range(self.next_index - i):
                cur_nonsorted_item = self.pop()
                if cur_nonsorted_item > largest:
                    largest = cur_nonsorted_item
                intermediate_stack.push(cur_nonsorted_item)
            self.push(largest)
            counter_of_doubles = 0
            while intermediate_stack.next_index != 0:
                cur_returned = intermediate_stack.pop()
                if largest != cur_returned:
                    self.push(cur_returned)
                elif (largest == cur_returned) and (counter_of_doubles != 0):
                    counter_of_doubles += 1
                    self.push(cur_returned)
                else:
                    continue

    def select_sort_ascending(self) -> None:
        """
    :return: сортирует по возврастанию посредством сортировки выбора
        """
        # создаём промежуточный стек
        intermediate_stack = ArrayStack(self.count)
        # выбираем наименьший элемент столько раз, сколько элементов есть в стеке
        for i in range(self.next_index):
            # помечаем наименьший элемент
            least = self.get_last_item()
            # проходимся по всем неотсортированным элементам и отправляем их в промежуточный стек
            for j in range(self.next_index - i):
                cur_returned = self.pop()
                if cur_returned < least:
                    least = cur_returned
                intermediate_stack.push(cur_returned)
            self.push(least)
            counter_of_doubles = 0
            while intermediate_stack.next_index != 0:
                cur_returned = intermediate_stack.pop()
                if cur_returned != least:
                    self.push(cur_returned)
                else:
                    if counter_of_doubles == 0:
                        counter_of_doubles += 1
                        continue
                    else:
                        self.push(cur_returned)


if __name__ == '__main__':
    stack = SortedStacks()
    stack.push(3)
    stack.push(1)
    stack.push(5)
    stack.push(2)
    stack.push(4)
    stack.select_sort_ascending()
    stack.cut()
    print(stack)
