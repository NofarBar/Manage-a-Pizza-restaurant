import datetime
import time
from multiprocessing.pool import ThreadPool

class WaterManager:

    def __init__(self, queue_in, preparation_times):
        self.pool = ThreadPool(2)
        self.queue_in = queue_in
        self.preparation_times = preparation_times


    def make_dough(self,  task):
        print(f"Waiter starts serving pizza {task} at {datetime.datetime.now()}")
        time.sleep(2)
        print(f"Waiter starts finishes pizza {task} at {datetime.datetime.now()}")
        self.preparation_times[str(task)].append(time.time())

    def menage_water(self):
        while True:
            task = self.queue_in.get()
            if task is None:
                self.pool.close()
                self.pool.join()
                break
            self.pool.apply_async(self.make_dough, [task])