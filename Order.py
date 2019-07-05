import random
import string
from Constant import Constant
from Action import Action

class Order:

    def __init__(self, start, dest, time, status):
        self._name = 'O_'.join(random.choices(string.ascii_uppercase, k=1))
        self._time = time
        self._start = start
        self._dest = dest
        self._status = status
        self._isDelivered = False
        self._price = self.price()

    def price(self):
        if self._status == Constant.full:
            d = Constant.d_full
        else:
            d = Constant.d_empty

        C0 = Constant.C0
        r = Constant.r
        return d * (C0 + r * self.distance())

    def prior(self):
        time = self.time()
        alpha = Constant.alpha
        if self._status == Constant.full:
            Wc = Constant.Wc_full
        else:
            Wc = Constant.Wc_empty

        return Wc * (time ** alpha)

    def distance(self):
        return self._dest - self._start

    def start(self):
        return self._start

    def dest(self):
        return self._dest

    def value(self):
        return self.price() + self.prior()

    def setTime(self, value):
        self._time = value

    def setAction(self, action: Action):
        self._action = action

    def action(self):
        return self._action

    def time(self):
        return self._time

    def isDelivered(self):
        return self._isDelivered == True

    def deliver(self):
        self._isDelivered = True

    def __repr__(self):
        return \
            "Name: {} Start:{} Dest:{} Distance:{} Price:{} Prior:{} value:{}" \
                .format(self._name, self.start(), self.dest(), self.distance(), self.price(), self.prior(), self.value())

    def cost(self):
        return self.distance() * Constant.Km_cost

    @staticmethod
    def printAll(objects):
        represent = ""
        for item in objects:
            represent += repr(item) + '\n'
        return represent
