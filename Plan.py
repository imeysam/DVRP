from Action import Action
from Constant import Constant
from typing import List
import numpy as np


class Plan:
    def __init__(self, number_of_action: int, actions: List[Action]):
        self.actions = actions
        self.N = number_of_action
        self._value = self.value()

    def value(self):
        value = 0
        for i in range(len(self.actions)):
            action = self.actions[i]
            value += action.value() * ((self.N - i) ** Constant.alpha)
        return value

    def __repr__(self):
        represent = ""
        for action in self.actions:
            represent += repr(action) + '\n'
        return represent

    def skeleton(self):
        storage = []
        for i in range(len(self.actions)):
            action = self.actions[i]
            storage.append(action.storage())
        return storage

    @staticmethod
    def getBestOfPlans(*plans):
        plans = list(plans)
        values = np.array([plan.value() for plan in plans])
        best_value = np.argmax(values)
        return plans[best_value]
