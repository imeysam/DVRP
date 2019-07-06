from Constant import Constant


class Action:
    def __init__(self, order):
        self.order = order
        self._start = order.start()
        self._dest = order.dest()
        self._status = self.status()

    def __repr__(self):
        return repr(self.order)

    def status(self):
        if self.order.isDelivered():
            return Constant.ACTION_DELIVERY
        else:
            return Constant.ACTION_EMPTY_RIDER

    def statusName(self):
        if self.status() == Constant.ACTION_DELIVERY:
            return "ToDelivery"
        else:
            return "EmptyRide"

    def start(self):
        return self.order.start()

    def dest(self):
        return self.order.dest()

    def value(self):
        if self._status == Constant.ACTION_DELIVERY:
            return self.order.value() - self.order.cost()
        else:
            return self.order.cost()

    def order(self):
        return self.order()

    def setStorage(self, storage):
        self._storage = storage

    def storage(self):
        return self._storage

    def firstLimitation(self):
        return self.start() != self.dest()

    def secondLimitation(self, next_action=None):
        if next_action is not None:
            return self.dest() == next_action.start()
        else:
            return True
