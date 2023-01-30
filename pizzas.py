# This is a sample Python script.
import json
import logging
import sys
import time
from queue import Queue
from threading import Thread

from src.chefs_manager import DoughChefsManager
from src.oven_manager import OvenManager
from src.topping_chefs_manager import ToppingChefManager
from src.waiter_manger import WaterManager



def prepare_pizzas(orders):

    preparation_times = {}
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    water_manager = WaterManager(preparation_times)
    oven_chef = OvenManager(water_manager)
    topping_manager = ToppingChefManager(oven_chef)
    dough_chef_manager = DoughChefsManager(topping_manager, preparation_times)
    for order in orders:
        dough_chef_manager.add_task(order)
    start_time = time.time()
    dough_chef_manager.wait_for_all_task_to_end()
    topping_manager.wait_for_all_task_to_end()
    oven_chef.wait_for_all_task_to_end()
    water_manager.wait_for_all_task_to_end()
    end_time = time.time()


    print("\n\n -----Report-----")
    for order in orders:
        if str(order) in preparation_times:
            print(f"Preparation time for order {order} : {preparation_times[str(order)][1] -preparation_times[str(order)][0]}")
    print(f"Total preparation time {end_time - start_time}")

if __name__ == "__main__":
    arg = sys.argv
    orders = []
    for arg in sys.argv[1:]:
        orders.append(arg.split(","))
    prepare_pizzas(orders)
