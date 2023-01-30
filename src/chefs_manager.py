import datetime
import logging
import time
from multiprocessing.pool import ThreadPool


class DoughChefsManager:

    def __init__(self, next_station, preparation_times):
        self.pool = ThreadPool(2)
        self.next_station = next_station
        self.preparation_times = preparation_times
        self.error = False


    def make_dough(self, task):
        try:
            self.preparation_times[str(task)] = [time.time()]
            logging.info(f"Dough chef starts working on {task}  at  {datetime.datetime.now()}")
            time.sleep(7)
            logging.info(f"Dough chef done working on {task}  at {datetime.datetime.now()}")
            self.next_station.add_task(task)
        except Exception as e:
            del self.preparation_times[str(task)]
            logging.error(f"Could not prepare pizza {task} error: {e}")

    def add_task(self, task):
        self.pool.apply_async(self.make_dough, [task])

    def wait_for_all_task_to_end(self):
        self.pool.close()
        self.pool.join()


