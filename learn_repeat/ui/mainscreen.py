from tkinter import Frame, StringVar, Label, Button, BOTH

from learn_repeat.db import Db
from learn_repeat.scheduler import Scheduler
from learn_repeat.ui.addscreen import AddScreen
from learn_repeat.utils import get_item


class MainScreen(Frame):

    def __init__(self, window):
        super(MainScreen, self).__init__()
        window.title('Learn-Repeat')
        window.resizable(width=False, height=False)

        self.db = Db()
        self.schedule = Scheduler()
        # text for labels ----------------------------------------------------
        self.to_learn_exercise_text = StringVar()
        self.to_repeat_exercise_text = StringVar()
        self.to_repeat_rule_text = StringVar()
        # labels -------------------------------------------------------------
        self.to_learn_exercise_label = Label(
            self, width=60, textvariable=self.to_learn_exercise_text
        )
        self.to_repeat_exercise_label = Label(
            self, width=60, textvariable=self.to_repeat_exercise_text
        )
        self.to_repeat_rule_label = Label(
            self, width=60, textvariable=self.to_repeat_rule_text
        )
        # buttons ------------------------------------------------------------
        self.add_exercise_btn = Button(
            self, text='Add',
            command=lambda: self.call_add_screen(self.schedule,
                                                 self.to_learn_exercise_text)
        )
        self.exercise_learned_btn = Button(
            self, text='Learned', command=self.set_to_repeated
        )
        self.exercise_repeated_btn = Button(
            self, text='Repeated',
            command=lambda: self.get_next(self.to_repeat_exercise_text,
                                          self.schedule.exercises_to_repeat)
        )
        self.rule_repeated_btn = Button(
            self, text='Repeated',
            command=lambda: self.get_next(self.to_repeat_rule_text,
                                          self.schedule.rules_to_repeat)
        )

        self.main_screen()

    def main_screen(self):
        self.pack(fill=BOTH, expand=1)

        self.to_learn_exercise_text.set(self.schedule.exercise_to_learn)
        self.to_repeat_exercise_text.set(
            get_item(self.schedule.exercises_to_repeat, 0)
        )
        self.to_repeat_rule_text.set(
            get_item(self.schedule.rules_to_repeat, 0)
        )

        self.to_learn_exercise_label.grid(row=0, column=0, sticky='NSEW')
        self.to_repeat_exercise_label.grid(row=1, column=0, sticky='NSEW')
        self.to_repeat_rule_label.grid(row=2, column=0, sticky='NSEW')

        self.add_exercise_btn.grid(row=0, column=1, sticky='w' + 'e')
        self.exercise_learned_btn.grid(row=0, column=2)
        self.exercise_repeated_btn.grid(row=1, column=1, columnspan=2,
                                        sticky='w' + 'e')
        self.rule_repeated_btn.grid(row=2, column=1, columnspan=2,
                                    sticky='w' + 'e')

    @staticmethod
    def call_add_screen(inst, label_text):
        AddScreen(inst, label_text)

    def set_to_repeated(self):
        self.schedule.set_to_repeat()
        self.to_learn_exercise_text.set(self.schedule.exercise_to_learn)

    def get_next(self, item, items):
        self.schedule.set_next_to_repeat(items)
        item.set(items[0])

    def destroy(self):
        self.db.write(self.schedule)
        super(MainScreen, self).destroy()
