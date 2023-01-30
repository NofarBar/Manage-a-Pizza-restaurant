import datetime
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool


class OvenChefs:

    def __init__(self, queue_in, queue_out):
        self.pool = ThreadPool(1)
        self.queue_in = queue_in
        self.queue_out = queue_out


    def make_dough(self,  task):
        print(f"Oven chef starts working on {task}  at {datetime.datetime.now()}")
        time.sleep(7)
        print(f"Oven chef done working on {task}  at {datetime.datetime.now()}")
        self.queue_out.put(task)

    def manage_oven_Chef(self):
        while True:
            task = self.queue_in.get()
            if task is None:
                self.pool.close()
                self.pool.join()
                self.queue_out.put(None)
                break
            self.pool.apply_async(self.make_dough, [task])
