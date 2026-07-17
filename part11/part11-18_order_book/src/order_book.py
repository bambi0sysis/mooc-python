class Task:
    id = 0

    def __init__(self, description: str, name: str, workload: int):
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer = name
        self.workload = workload
        self.flag = False

    def __str__(self):
        S = "" if self.is_finished() else "NOT "
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {S}FINISHED"

    def is_finished(self):
        return self.flag

    def mark_finished(self):
        self.flag = True
        return True


class OrderBook:
    def __init__(self):
        self.__orders = []

    def add_order(self, description: str, name: str, workload: int):
        self.__orders.append(Task(description, name, workload))

    def all_orders(self):
        return self.__orders

    def programmers(self):
        names = list(set([order.programmer for order in self.__orders]))
        return names

    def mark_finished(self, id: int):
        for task in self.__orders:
            if task.id == id:
                task.mark_finished()
                break
        else:
            raise ValueError("task id doesnt exist")

    def finished_orders(self):
        finished_orders = []
        for task in self.__orders:
            if task.is_finished():
                finished_orders.append(task)
        return finished_orders

    def unfinished_orders(self):
        unfinished_orders = []
        for task in self.__orders:
            if not task.is_finished():
                unfinished_orders.append(task)
        return unfinished_orders

    def status_of_programmer(self, programmer: str):
        finished_orders = finished_workload_sum = unfinished_orders = (
            unfinished_orders_workload_sum
        ) = 0
        flag = False
        for task in self.__orders:
            if task.programmer != programmer:
                continue
            if task.is_finished():
                flag = True
                finished_orders += 1
                finished_workload_sum += task.workload
            else:
                flag = True
                unfinished_orders += 1
                unfinished_orders_workload_sum += task.workload
        if not flag:
            raise ValueError("programmer aint in the task list")
        return (
            finished_orders,
            unfinished_orders,
            finished_workload_sum,
            unfinished_orders_workload_sum,
        )
