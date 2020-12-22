from tkinter import *
from lists import list_methods as lm
from functools import partial


class Example(Tk):

    # standard footer button
    but = {
        'fg': 'white',
        'bg': 'black',
        'borderwidth': 2,
        'relief': GROOVE,
        'side': RIGHT,
        'padx': 10,
        'pady': 10,
        'fill': Y
    }
    but_text = ["Create list", "Add cell"]
    cell = {
        'position_y': 60,
        'width': 20,
        'height': 20,
        'position_x': 40,
        'ident': 20,
        'text_bias_x': 10,
        'text_bias_y': 10
    }

    null_cell = {
        'bias_y': 3,
        'height': 15
        ,
        'width': 15,
        'bg': 'grey'
    }

    def __init__(self):
        super().__init__()
        self.initUI()
        self.onedirect_list = lm.List()
        self.last_cell_list_x = 0
        self.last_cell_list_y = 0

    def initUI(self):
        # custom window's settings
        self.geometry("800x800")
        self.resizable(width=FALSE, height=FALSE)

        canvas_frame = Frame(master=self, height=650, bg="white", borderwidth=5, relief="groove")
        canvas_frame.pack(fill=X)
        canvas_frame.pack_propagate(FALSE)
        canvas_object = Canvas(master=canvas_frame, height=650, bg="white")
        canvas_object.pack(fill=BOTH)

        footer = Frame(master=self, height=80, bg="grey", borderwidth=5, relief="sunken")
        footer.pack(fill=BOTH, padx=10, pady=15)
        footer.pack_propagate(FALSE)

        by_first_button = partial(self.add_list, canvas_object)
        for i in range(len(Example.but_text)):
            button_generate = Button(master=footer, text=Example.but_text[i], fg=Example.but['fg'],\
                                     bg=Example.but['bg'], borderwidth=Example.but['borderwidth'],\
                                     relief=Example.but['relief'], command=by_first_button)

            button_generate.pack(side=Example.but["side"], padx=Example.but["padx"], pady=Example.but["pady"],\
                                 fill=Example.but["fill"])

    def add_list(self, c):
        if self.onedirect_list.pointer.next is not None:
            c.delete("block")
            c.delete("block_text")
            c.delete("null")
            c.delete("arrow")
            self.onedirect_list.pointer.next = None
        self.onedirect_list.random_list()

        c.create_text(60, 30, text="Random list")

        x1_coord = Example.cell['position_x']  # x1 coord
        y1_coord = Example.cell['position_y']  # y1 coord
        x2_coord = Example.cell['position_x'] + Example.cell['width']  # x2 coord
        y2_coord = Example.cell['position_y'] + Example.cell['height']  # y2 coord

        c.create_rectangle(
            x1_coord,  # x1 coord
            y1_coord,  # y1 coord
            x2_coord,  # x2 coord
            y2_coord,  # y2 coord
            fill="black",
            tag='sentinel'
        )
        c.create_line(
            x2_coord,
            y2_coord - Example.cell['height'] // 2,
            x2_coord + Example.cell['ident'],
            y2_coord - Example.cell['height'] // 2,
            arrow=LAST,
            tag="arrow"
        )

        x1_coord += Example.cell['width'] + Example.cell['ident']
        x2_coord += Example.cell['width'] + Example.cell['ident']

        values = self.onedirect_list.generator_print()
        for val in values:
            c.create_rectangle(
                x1_coord,
                y1_coord,
                x2_coord,
                y2_coord,
                fill="orange",
                tag="block"
            )
            c.create_text(x1_coord + Example.cell['text_bias_x'],
                          y1_coord + Example.cell['text_bias_y'],
                          text=val,
                          tag="block_text")

            c.create_line(
                x2_coord,
                y2_coord - Example.cell['height'] // 2,
                x2_coord + Example.cell['ident'],
                y2_coord - Example.cell['height'] // 2,
                arrow=LAST,
                tag="arrow"
            )

            x1_coord += Example.cell['width'] + Example.cell['ident']
            x2_coord += Example.cell['width'] + Example.cell['ident']

        c.create_rectangle(
            x1_coord,
            y1_coord + Example.null_cell['bias_y'],
            x1_coord + Example.null_cell['width'],
            y1_coord + Example.null_cell['bias_y'] + Example.null_cell['height'],
            fill=Example.null_cell['bg'],
            tag="null"
        )


if __name__ == "__main__":
    window = Example()
    window.mainloop()
