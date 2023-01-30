import datetime
import logging
import time
from multiprocessing.pool import ThreadPool


class WaterManager:

    def __init__(self,  preparation_times):
        self.pool = ThreadPool(2)
        self.preparation_times = preparation_times

    def serve_pizza(self, task):
        try:
            logging.info(f"Waiter starts serving pizza {task} at {datetime.datetime.now()}")
            time.sleep(5)
            logging.info(f"Waiter starts finishes pizza {task} at {datetime.datetime.now()}")
            self.preparation_times[str(task)].append(time.time())
        except Exception as e:
            logging.error(f"Could not prepare pizza {task} error: {e}")

    def add_task(self, task):
        self.pool.apply_async(self.serve_pizza, [task])

    def wait_for_all_task_to_end(self):
        self.pool.close()
        self.pool.join()
