from tkinter import Frame, StringVar, Label, Button, BOTH

from learn_repeat.db import read, write
from learn_repeat.scheduler import Exercise, Rule
from learn_repeat.ui.addscreen import AddScreen
from learn_repeat.utils import get_item


class MainScreen(Frame):

    def __init__(self, window):
        super(MainScreen, self).__init__()
        window.title('Learn-Repeat')
        window.resizable(width=False, height=False)

        self.exercise, self.rule = read() or (Exercise(), Rule())
        # text for labels ----------------------------------------------------
        self.to_learn_exercise_text = StringVar()
        self.to_repeat_exercise_text = StringVar()
        self.to_learn_rule_text = StringVar()
        self.to_repeat_rule_text = StringVar()
        # labels -------------------------------------------------------------
        self.to_learn_exercise_label = Label(
            self, width=60, textvariable=self.to_learn_exercise_text
        )
        self.to_repeat_exercise_label = Label(
            self, width=60, textvariable=self.to_repeat_exercise_text
        )
        self.to_learn_rule_label = Label(
            self, width=60, textvariable=self.to_learn_rule_text
        )
        self.to_repeat_rule_label = Label(
            self, width=60, textvariable=self.to_repeat_rule_text
        )
        # buttons ------------------------------------------------------------
        self.add_exercise_btn = Button(
            self, text='Add',
            command=lambda: self.call_add_screen(self.exercise,
                                                 self.to_learn_exercise_text)
        )
        self.exercise_learned_btn = Button(
            self, text='Learned', command=lambda: self.set_to_repeated(
                self.exercise, self.to_learn_exercise_text)
        )
        self.exercise_repeated_btn = Button(
            self, text='Repeated',
            command=lambda: self.get_next(self.to_repeat_exercise_text,
                                          self.exercise)
        )
        self.add_rule_btn = Button(
            self, text='Add',
            command=lambda: self.call_add_screen(self.rule,
                                                 self.to_learn_rule_text)
        )
        self.rule_learned_btn = Button(
            self, text='Learned', command=lambda: self.set_to_repeated(
                self.rule, self.to_learn_rule_text)
        )
        self.rule_repeated_btn = Button(
            self, text='Repeated',
            command=lambda: self.get_next(self.to_repeat_rule_text,
                                          self.rule)
        )

        self.main_screen()

    def main_screen(self):
        self.pack(fill=BOTH, expand=1)

        self.to_learn_exercise_text.set(self.exercise.item_to_learn)
        self.to_repeat_exercise_text.set(
            get_item(self.exercise.items_to_repeat, 0)
        )
        self.to_learn_rule_text.set(self.rule.item_to_learn)
        self.to_repeat_rule_text.set(
            get_item(self.rule.items_to_repeat, 0)
        )

        self.to_learn_exercise_label.grid(row=0, column=0, sticky='NSEW')
        self.to_repeat_exercise_label.grid(row=1, column=0, sticky='NSEW')
        self.to_learn_rule_label.grid(row=2, column=0, sticky='NSEW')
        self.to_repeat_rule_label.grid(row=3, column=0, sticky='NSEW')

        self.add_exercise_btn.grid(row=0, column=1, sticky='w' + 'e')
        self.exercise_learned_btn.grid(row=0, column=2)
        self.exercise_repeated_btn.grid(row=1, column=1, columnspan=2,
                                        sticky='w' + 'e')
        self.add_rule_btn.grid(row=2, column=1, sticky='w' + 'e')
        self.rule_learned_btn.grid(row=2, column=2)
        self.rule_repeated_btn.grid(row=3, column=1, columnspan=2,
                                    sticky='w' + 'e')

    @staticmethod
    def call_add_screen(inst, label_text):
        AddScreen(inst, label_text)

    @staticmethod
    def set_to_repeated(item, label_text):
        item.set_to_repeat()
        label_text.set(item.item_to_learn)

    @staticmethod
    def get_next(label_text, item):
        item.set_next_to_repeat()
        label_text.set(item.items_to_repeat[0])

    def destroy(self):
        write((self.exercise, self.rule))
        super(MainScreen, self).destroy()
