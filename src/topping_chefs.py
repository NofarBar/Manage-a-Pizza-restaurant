import datetime
import time
from multiprocessing.pool import ThreadPool


class ToppingChef:

    def __init__(self, queue_in, queue_out):
        self.pool = ThreadPool(2)
        self.queue_in = queue_in
        self.queue_out = queue_out

    def make_dough(self,  task):
        print(f"Topping chef starts working on topping {task}  at {datetime.datetime.now()}")
        time.sleep(7)
        print(f"Topping chef done  working on topping {task}  at {datetime.datetime.now()}")
        return task

    def manege_toppingChef(self):
        while True:
            task = self.queue_in.get()
            if task is None:
                self.pool.close()
                self.pool.join()
                self.queue_out.put(None)
                break
            toppings = [task[i:i + 2] for i in range(0, len(task), 2)]
            self.pool.map_async(self.make_dough, toppings, callback=self.finish_topping_callback)

    def finish_topping_callback(self, task):
        full_pizza = []
        for t in task:
            full_pizza+=t
        self.queue_out.put(full_pizza)




