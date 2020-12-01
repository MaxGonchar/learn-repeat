from abc import ABC
from collections import deque


class Scheduler(ABC):

    def __init__(self):
        self.item_to_learn = 'None'
        self.items_to_repeat = deque([])

    def set_to_learn(self, item):
        self.item_to_learn = item

    def set_to_repeat(self):
        self.items_to_repeat.append(self.item_to_learn)
        self.item_to_learn = 'None'

    def set_next_to_repeat(self):
        self.items_to_repeat.rotate(-1)


class Exercise(Scheduler):
    pass


class Rule(Scheduler):
    pass
