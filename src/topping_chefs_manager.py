import datetime
import logging
import time
from multiprocessing.pool import ThreadPool


class ToppingChefManager:

    def __init__(self, next_station):
        self.pool = ThreadPool(3)
        self.next_station = next_station

    def add_toppings(self, task):
        try:
            logging.info(f"Topping chef starts working on topping {task}  at {datetime.datetime.now()}")
            time.sleep(4)
            logging.info(f"Topping chef done  working on topping {task}  at {datetime.datetime.now()}")
            return task
        except Exception as e:
            logging.error(f"Could not prepare pizza {task} error: {e}")

    def finish_topping_callback(self, task):
        full_task = []
        for t in task:
            if task is None:
                return
            full_task += t
        self.next_station.add_task(full_task)

    def add_task(self, task):
        toppings = [task[i:i + 2] for i in range(0, len(task), 2)]
        self.pool.map_async(self.add_toppings, toppings, callback=self.finish_topping_callback)

    def wait_for_all_task_to_end(self):
        self.pool.close()
        self.pool.join()





