from tkinter import Toplevel, StringVar, Entry, Button


class AddScreen(Toplevel):

    def __init__(self, inst, label_text):
        super(AddScreen, self).__init__()
        self.resizable(width=False, height=False)
        self.grab_set()
        self.label_text = label_text
        self.inst = inst
        self.input_text = StringVar()

        self.text_field = Entry(
            self, width=60, textvariable=self.input_text
        )
        self.add_btn = Button(
            self, text='Add', command=self._set_item
        )

        self._add_screen()

    def _add_screen(self):
        self.text_field.grid(row=0, column=0)
        self.add_btn.grid(row=0, column=1)

    def _set_item(self):
        self.inst.set_to_learn(self.input_text.get())
        self.label_text.set(self.input_text.get())
        self.destroy()
