from helpers.helpers import *
from tkinter import *
from trees.binary_tree import *


class BinaryTreeGUI(Tk):
    def __init__(self, tree: BinaryTree, width=800, height=800):
        super().__init__()

        self.w_width: float = width
        self.w_height: float = height

        self.header_height: float = self.w_height / 6

        self.level_height: float = (height - self.header_height) / tree.levels()


        self.tree: BinaryTree = tree

        self.settings()

        self.header()

        self.set_tree()

    def set_tree(self):

        queue_of_parents = Queue()
        # Creating of the canvas
        canvas = Canvas(master=self, bg='yellow', height=self.w_height - self.header_height)
        canvas.pack(fill=X, expand=True)

        radius = self.circle_radius()

        # Pass through levels
        for cur_level in range(1, self.tree.levels() + 1):

            # Getting the width of the node's cell
            cur_cell_width = self.define_width_of_circles_cell(cur_level)

            y1 = (cur_level - 1) * self.level_height
            y2 = cur_level * self.level_height - 1

            if cur_level == self.tree.levels():
                sentinel = self.tree.terminal_cells()
            else:
                sentinel = 2 ** (cur_level - 1)

            # pass through cells of the cur level
            for bias in range(sentinel):

                x1 = bias * cur_cell_width
                x2 = (bias + 1) * cur_cell_width

                x_mid, y_mid = BinaryTreeGUI.find_mid(x1, y1, x2, y2)

                canvas.create_oval(x_mid - radius, y_mid - radius, x_mid + radius, y_mid + radius, fill='orange')

                if queue_of_parents != 0:
                    queue_of_parents.check()['bind_count'] += 1

                    if queue_of_parents.check()['bind_count'] == 2:
                        parent_values = queue_of_parents.pop()
                    else:
                        parent_values = queue_of_parents.check()

                    canvas.create_line(x_mid, y_mid - radius, parent_values['bind_x'], parent_values['bind_y'])

                canvas.create_text(x_mid, y_mid, anchor=CENTER, text=self.tree.cell_by_data(cur_level, bias).name)

                parent_values = {
                                'bind_x': x_mid,
                                'bind_y': y_mid + radius,
                                'bind_count': 0
                                 }

                queue_of_parents.push(parent_values)




    def define_width_of_circles_cell(self, level: int):
        return self.w_width / (2 ** (level - 1))

    def settings(self):
        #self.resizable(width=FALSE, height=FALSE)
        self.geometry('{}x{}'.format(self.w_width, self.w_height))
        self.config(bg="white")

    def header(self):
        header = Frame(master=self, bg="green", height=self.header_height)
        header.pack(fill=X)

    def body(self):
        pass

    def circle_radius(self):
        width_of_last_cell = self.define_width_of_circles_cell(self.tree.levels())
        radius = min(width_of_last_cell, self.level_height) * 0.8 / 2
        return radius


    @staticmethod
    def find_mid(x1, y1, x2, y2):
        return (x1 + x2) / 2, (y1 + y2) / 2


class DragAndDropArea(Canvas):
    pass
    # bind('<ButtonPress-1>')
    # self.bind('<B1-Motion>')
    # self.bind('<ButtonRelease-1>')


if __name__ == '__main__':
    tree = BinaryTree.generate_random_tree()
    tree.print_tree()
    obj = BinaryTreeGUI(tree)
    obj.mainloop()
