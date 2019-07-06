from Truck import Truck
from Storage import Storage
from Constant import Constant
from typing import List
import numpy as np


class PlanLEM:
    def __init__(self, number_of_storage: int, truck: Truck, storage: List[Storage]):
        self._truck = truck
        self._storage = storage
        self.N = number_of_storage
        self._plans = [truck.bestAction(storage[0])]
        for i in range(len(storage)-1):
            self._plans.append(storage[i].bestAction(storage[1+1]))

    def __repr__(self):
        represent = ""
        for storage in self._storage:
            represent += repr(storage) + '\n'
        return represent

    def value(self):
        balance = 0
        balance += self._truck.bestAction(self._storage[0]) * (self.N ** Constant.alpha)
        for i in range(len(self._storage)-1):
            balance += self._storage[i].bestAction(self._storage[1+1]) * ((i-1) ** Constant.alpha)
        return balance

    @staticmethod
    def getBestOfPlans(*plans):
        plans = list(plans)
        values = np.array([plan.value() for plan in plans])
        best_value = np.argmax(values)
        return plans[best_value]


