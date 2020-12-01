from collections import deque

from learn_repeat.db import Db


class Scheduler:

    def __init__(self):
        self.db = Db()
        self.inst = self.db.read()
        try:
            self.exercise_to_learn = self.inst.exercise_to_learn
        except AttributeError:
            self.exercise_to_learn = 'None'
        try:
            self.exercises_to_repeat = self.inst.exercises_to_repeat
        except AttributeError:
            self.exercises_to_repeat = deque([])
        try:
            self.rules_to_repeat = self.inst.rules_to_repeat
        except AttributeError:
            self.rules_to_repeat = deque([])

    def set_to_learn(self, exercise):
        self.exercise_to_learn = exercise

    def set_to_repeat(self):
        self.exercises_to_repeat.append(self.exercise_to_learn)
        self.exercise_to_learn = None

    @staticmethod
    def set_next_to_repeat(deque_):
        deque_.rotate(-1)
