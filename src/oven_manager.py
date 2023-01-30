import datetime
import logging
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool


class OvenManager:

    def __init__(self, next_station):
        self.pool = ThreadPool(1)
        self.next_station = next_station

    def cook_pizza(self, task):
        try:
            logging.info(f"Oven chef starts working on {task}  at {datetime.datetime.now()}")
            time.sleep(10)
            logging.info(f"Oven chef done working on {task}  at {datetime.datetime.now()}")
            self.next_station.add_task(task)
        except Exception as e:
            logging.error(f"Could not prepare pizza {task} error: {e}")

    def add_task(self, task):
        self.pool.apply_async(self.cook_pizza, [task])

    def wait_for_all_task_to_end(self):
        self.pool.close()
        self.pool.join()