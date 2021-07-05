from tkinter import *
from stacks_and_deques.applied_stack.hanoi.hanoi import Hanoi
from functools import partial
from typing import List
from stacks_and_deques.applied_stack.hanoi.event_func import block_event, layer_event


class Game(Tk):
    def __init__(self, width=800, height=800, count_of_sides=3):
        # инициализируем Tkinter
        super().__init__()

        # задаём размеры окна
        self.width: int = width
        self.height: int = height

        # задаём фон и опору для колышек
        self.make_window()
        self.make_floor()

        # количество колышек/прамидок
        self.count_of_sides: int = count_of_sides

        # тут храним слои, где будут размещаться пирамидки
        self.layers: List[Frame] = []

        # создаём деление на слои
        self.make_scene()
        # рисуем колышки
        self.make_sticks()

        self.stacks: List[Hanoi] = []
        # создаём стеки
        self.make_stacks()

        # создаём функции нажатия на блоки и слои
        self.construct_binds()

    # создаётся и разукрашиваетя окно нужных размеров
    def make_window(self):
        self.geometry('{}x{}'.format(self.width, self.height))
        self['bg'] = 'white'
        self.resizable(False, False)

    # рисуется пол
    def make_floor(self):
        self.floor = Frame(master=self, bg='brown', height=self.height / 5)
        self.floor.pack(fill=X, side=BOTTOM)

    # заполняются и отрисовываются слои
    def make_scene(self):
        for i in range(self.count_of_sides):
            self.layers.append(Frame(master=self, bg='white', width=self.width / self.count_of_sides))
            self.layers[i].pack(fill=Y, side=LEFT)

    # просто отрисовываются палки
    def make_sticks(self):
        for i in range(self.count_of_sides):
            Canvas(master=self.layers[i], bg='orange').place(relwidth=0.05, relheight=0.5, rely=0.5,
                                                             relx=0.5 - 0.05 / 2)

    # привязки к кнопкам и слоям
    def construct_binds(self):
        # для каждого блока создаём привязку по нажатию, в которую передаётся событие и сам блок
        for i in range(5):
            event_for_block = partial(block_event, self.stacks[0].array[i])
            self.stacks[0].array[i].frame.bind("<Button-1>", event_for_block)

        # аналогично для каждого слоя создаём привязку, в которую передаём событие, массив блоков и массив слоёв
        event_for_layer = partial(layer_event, self.all_blocks, self.stacks, self.width)
        for i in range(self.count_of_sides):
            self.layers[i].bind('<Button-1>', event_for_layer)

    def make_stacks(self):
        # сохраняем стеки
        self.stacks.extend([Hanoi(self.layers[i]) for i in range(self.count_of_sides)])
        # заполняем крайний левый стек
        self.stacks[0].fill_array()
        # каждый блок может следить за состоянием других созданных блоков с помощью атрибута all_statuses
        for i in range(self.stacks[0].count):
            self.stacks[0].array[i].__dict__['all_statuses'] =\
                [self.stacks[0].array[j] for j in range(self.stacks[0].count)]
        # аналогичным образом за состоянием блоков может следить объект игры
        self.all_blocks = [self.stacks[0].array[j] for j in range(self.stacks[0].count)]


if __name__ == "__main__":
    new = Game()
    new.mainloop()