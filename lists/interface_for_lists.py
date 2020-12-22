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

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.geometry("800x800")
        self.resizable(width=FALSE, height=FALSE)
        canvas_frame = Frame(master=self, height=650, bg="white", borderwidth=5, relief="groove")
        canvas_frame.pack(fill=X)
        canvas_frame.pack_propagate(FALSE)
        footer = Frame(master=self, height=80, bg="grey", borderwidth=5, relief="sunken")
        footer.pack(fill=BOTH, padx=10, pady=15)
        footer.pack_propagate(FALSE)
        by_first_button = partial(Example.add_list, canvas_frame)

        for i in range(len(Example.but_text)):
            button_generate = Button(master=footer, text=Example.but_text[i], fg=Example.but['fg'],\
                                     bg=Example.but['bg'], borderwidth=Example.but['borderwidth'],\
                                     relief=Example.but['relief'], command=by_first_button)

            button_generate.pack(side=Example.but["side"], padx=Example.but["padx"], pady=Example.but["pady"],\
                                 fill=Example.but["fill"])

    @staticmethod
    def add_list(frame):
        new_list = lm.List()
        new_list.add_nodes(*[1, 2, 5, 4])
        c = Canvas(master=frame, height=650, bg="white")
        c.create_text(60, 30, text="Random list")
        values = new_list.generator_print()
        i = 0
        for val in values:
            c.create_rectangle(
                20 + i * 40, 60, 40 + i * 40, 80,
                fill="orange",
            )
            c.create_text(28 + i * 40, 68, text=val)
            i += 1

        c.pack(fill=BOTH)


if __name__ == "__main__":
    window = Example()
    window.mainloop()
