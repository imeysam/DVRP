from Order import Order
from Truck import Truck
from Action import Action
from Plan import Plan
from PlanLEM import PlanLEM
from Storage import Storage
from typing import List
import numpy as np


class ApproachFirst:

    @staticmethod
    def getBestOrder(trunk: Truck, orders: List[Order]):
        orders_values = np.array([(order.value() - order.cost() + trunk.costToOrderStart(order)) for order in orders])
        best_value = np.argmax(orders_values)
        return orders[best_value]


class ApproachSecond:

    @staticmethod
    def getBestPlan(trunk: Truck, orders: List[Order]):
        actions = []
        for order in orders:
            action = Action(order)
            order.setAction(action)
            actions.append(action)

        plan_1 = Plan(len(actions), actions)
        plan_2 = Plan(len(actions), actions)
        plan_3 = Plan(len(actions), actions)

        best_plan = Plan.getBestOfPlans(plan_1, plan_2, plan_3)

        trunk.setPlan(best_plan)
        return best_plan


class ApproachThird:

    @staticmethod
    def getBestPlan(trunk: Truck, orders: List[Order]):
        actions = []
        storage = []
        for order in orders:
            action = Action(order)
            order.setAction(action)
            storage_temp = Storage(action)
            actions.append(action)
            storage.append(storage_temp)

        plan_1 = PlanLEM(len(storage), trunk, storage)
        plan_2 = PlanLEM(len(storage), trunk, storage)
        plan_3 = PlanLEM(len(storage), trunk, storage)

        best_plan = PlanLEM.getBestOfPlans(plan_1, plan_2, plan_3)
        return best_plan
