import random
import string
from Order import Order
from Plan import Plan


class Truck:
    def __init__(self, position):
        self._name = ''.join(random.choices(string.ascii_uppercase, k=1))
        self._position = position

    def __repr__(self):
        return "{} in {}".format(self.name(), self.position())

    def name(self):
        return self._name

    def position(self):
        return self._position

    def costToOrderStart(self, order: Order):
        return abs(self.position() - order.start())

    def setPlan(self, plan: Plan):
        self._plan = plan

    def plan(self):
        return self._plan

    @staticmethod
    def printAll(objects):
        for item in objects:
            print(item)
