from tkinter import *

class Interface(Tk):
    width_cell = 50
    height_cell = 50

    def __init__(self, count, typeof='int', width=900, height=900):
        super().__init__()
        self.set_attributes(count, typeof, width, height)
        self.make_grid()
        self.create_array()
        self.mainloop()

    def set_attributes(self, count, typeof, width, height):
        self.count = count
        self.typeof = typeof
        self.title("App for sorting of arrays")
        self.geometry(f"{width}x{height}".format(width=width, height=height))
        self.resizable(False, False)
        self.config(bg='white')

    def make_grid(self):
        self.columnconfigure([0, 1, 2], weight=1)
        self.rowconfigure(0, weight=1)
        self.working_array = Frame(master=self, bg='white')
        self.working_array.grid(row=0, column=0, columnspan=2, sticky="nswe")
        self.code_frame = Frame(master=self, bg="red")
        self.code_frame.grid(row=0, column=2, sticky="nswe")
        self.update()

    def create_array(self):
        length = self.count * (Interface.width_cell + 2)
#       array = Frame(master=self.working_array, height=Interface.height_cell, width=length, bg='orange')
        newr = Frame(master=self.working_array, bg='orange', height=Interface.height_cell)
        newr.pack(fill=X, padx=20, pady=70)
        print(self.working_array.winfo_width())
        print(self.code_frame.winfo_width())

    def create_cells(self):
        for i in range(self.count):
            pass

    def find_length_of_array(self):
        pass

    def draw_all(self):
        pass


if __name__ == '__main__':
    interface = Interface(5)
