# This is a sample Python script.
import json
import logging
import sys
import time
from queue import Queue
from threading import Thread

from src.chefs import Chefs
from src.oven_chef import OvenChefs
from src.topping_chefs import ToppingChef
from src.water_manger import WaterManager


def prepare_pizzas(orders):
    dough_queue = Queue()
    topping_queue = Queue()
    oven_queue = Queue()
    water_queue = Queue()
    preparation_times = {}

    chefManeger = Chefs(dough_queue, topping_queue, preparation_times)
    ovenChef = OvenChefs(oven_queue, water_queue)
    toppingManager = ToppingChef(topping_queue, oven_queue)
    waterManager = WaterManager(water_queue, preparation_times)
    for order in orders:
        dough_queue.put(order)

    start_time = time.time()
    dough_chef_1 = Thread(target=chefManeger.menage_Chefs, args=())
    dough_chef_1.start()
    topping_chef_1 = Thread(target=toppingManager.manege_toppingChef, args=())
    topping_chef_1.start()
    oven_thread = Thread(target=ovenChef.manage_oven_Chef, args=())
    oven_thread.start()
    water_thread = Thread(target=waterManager.menage_water, args=())
    water_thread.start()
    dough_chef_1.join()
    topping_chef_1.join()
    oven_thread.join()
    water_thread.join()
    end = time.time()

    print("\n\n -----Report-----")
    for order in orders:
        print(f"preparation time for order {order} : {preparation_times[str(order)][1] - preparation_times[str(order)][0]}")
    print(f"Total preparation time {end - start_time}")

if __name__ == "__main__":
    arg = sys.argv
    orders = []
    for arg in sys.argv[1:]:
        orders.append(arg.split(","))
    prepare_pizzas(orders)
