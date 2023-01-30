import datetime
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool


class Chefs:

    def __init__(self, queue_in, queue_out, preparation_times):
        self.pool = ThreadPool(2)
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.preparation_times = preparation_times


    def make_dough(self,  task):
        self.preparation_times[str(task)] = [time.time()]
        print(f"Dough chef starts working on {task}  at  {datetime.datetime.now()}")
        time.sleep(7)
        print(f"Dough chef done working on {task}  at {datetime.datetime.now()}")
        self.queue_out.put(task)

    def menage_Chefs(self):
        while True:
            if self.queue_in.empty():
                self.pool.close()
                self.pool.join()
                self.queue_out.put(None)
                break
            task = self.queue_in.get()
            self.pool.apply_async(self.make_dough, [task])



