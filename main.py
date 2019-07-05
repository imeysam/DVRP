from Order import Order
from Truck import Truck
from Assistant import ApproachFirst, ApproachSecond
from random import randint

if __name__ == "__main__":

    orders = []
    for i in range(10):
        temp = Order(randint(0, 9), randint(9, 20), randint(50, 100), 1)
        orders.append(temp)

    truck = Truck(randint(0, 20))

    print("All Orders are: ")
    print(Order.printAll(orders))



    ####################################### FIRST APPROACH ##########################################
    print("Approach 1: {}" . format(ApproachFirst.getBestOrder(truck, orders)))


    ####################################### SECOND APPROACH ##########################################
    print(ApproachSecond.getBestPlan(truck, orders))
