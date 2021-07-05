from typing import List, Optional
from random import choice
from tkinter import Frame
from stacks_and_deques.applied_stack.hanoi.event_func import block_event
from functools import partial


# класс отвечает за хранение всех характерчти блока
class Block:
    def __init__(self, val: Optional[int], index: int, parent: Frame, parent_stack):
        # значение ячейки. чем оно меньше, тем больше его объем
        self.value: Optional[int] = val
        # выбираем рандомный цвет
        self.color = choice(['red', 'yellow', 'green', 'blue'])
        # задаём фиксированную высоту
        self.height=0.05
        # номер ячейки для отслеживания позиции в стеке и задания высоты
        self.index = index
        # слой, в котором размещается ячейка
        self.parent = parent
        # ссылка на стек, которому принадлежит блок
        self.parent_stack: Hanoi = parent_stack
        # сам фрейм
        self.frame = Frame(master=self.parent, bg=self.color,  highlightthickness=1, highlightbackground="black")

        self.block_status = 0

    # автоматически вычисляется ширина
    @property
    def width(self) -> float:
        return 0.5 - 0.08 * (self.value - 1)

    # автоматически вычисляется смешение блока к центру
    @property
    def width_offset(self) -> float:
        return 0.25 + 0.04 * (self.value - 1)

    # нахождение блока по высоте
    @property
    def y_offset(self):
        return 1 - (self.index + 1) * 0.05

    # отображение блока
    def visual_block(self):
        self.frame.place(relwidth=self.width, relheight=self.height, relx=self.width_offset, rely=self.y_offset)

    # удаление блока
    def destroy(self):
        self.frame.destroy()

    # сравнение блоков
    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value

    def __str__(self) -> str:
        return str(self.value)


class Hanoi:
    def __init__(self, parent: Frame, nums: int = 5):
        # количество места для блоков
        self.count: int = nums
        # счётчик заполнения стека
        self.next_index: int = 0
        # родитель-слой
        self.parent_frame: Frame = parent
        # выделяем память под блоки
        self.array: List[Optional[Block]] = [None for i in range(self.count)]

    # создание полного столбца блоков и их заполнение
    def fill_array(self):
        for i in range(1, self.count+1):
            new_block: Block = Block(i, self.next_index, self.parent_frame, self)
            self.push(new_block)

    def pop(self) -> Optional[Block]:
        if self.next_index == 0:
            raise ValueError("NO")
        # получаем последний элемент
        last_item: Block = self.array[self.next_index - 1]
        # удаляем его
        self.array[self.next_index - 1].destroy()
        self.array[self.next_index - 1] = None
        # смещаем индекс
        self.next_index -= 1

        return last_item

    def push(self, item: Block):
        # если стек перезабит - выкидываем исключение (хотя такое произойти не может)
        if self.next_index == self.count:
            raise ValueError("NO!")
        else:
            # если этот стек не пуст - начинаем сравнение ячеек
            if self.next_index != 0:
                # получаем последний элемент текущего стека
                last_item: Block = self.get_without_delete()
                # если значение старого блока больше нового
                if last_item > item:
                    # тогда возвращаем блок с родительский стек
                    item.parent_stack.push(item)
                    # прерываем работу
                    return None
            # если всё прошло удачно - адаптируем блок
            self.adapt_frame(item)
            # записываем его
            self.array[self.next_index] = item
            # выводим
            item.visual_block()
            # и увеличиваем счётчик
            self.next_index += 1

    # просто получает последний элемент
    def get_without_delete(self):
        return self.array[self.next_index - 1]

    # выводим всю башню
    def visual_tower(self):
        for i in range(self.next_index):
            self.array[i].visual_block()

    # для адаптации блока под новый стек
    def adapt_frame(self, block: Block):
        # если блок находится не в слое стека
        if block.parent != self.parent_frame:
            # исправляем эту ситуацию
            block.parent = self.parent_frame
        # если индекс блока не совпадает с текущем индексом контейнера
        if block.index != self.next_index:
            # исправляем эту ситуацию
            block.index = self.next_index
        # указываем блоку ссулку на его новый стек
        block.parent_stack = self
        # перезаписываем фрейм
        block.frame = Frame(self.parent_frame, bg=block.color, highlightthickness=1, highlightbackground="black")
        # привязываем событие для блока
        event_for_block = partial(block_event, block)
        block.frame.bind('<Button-1>', event_for_block)

    def __str__(self) -> str:
        return str(self.array)


if __name__ == '__main__':
    pass
