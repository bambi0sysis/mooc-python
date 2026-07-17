class Task:
    id = 0

    @classmethod
    def new_id(self):
        Task.id += 1
        return Task.id

    def __init__(self, description: str, name: str, workload: int):
        self.id = Task.new_id()
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
        return [t for t in self.__orders if t.is_finished()]

    def unfinished_orders(self):
        return [t for t in self.__orders if not t.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("programmer aint in the task list")
        finished_orders = finished_workload_sum = unfinished_orders = (
            unfinished_orders_workload_sum
        ) = 0
        for task in self.__orders:
            if task.programmer != programmer:
                continue
            if task.is_finished():
                finished_orders += 1
                finished_workload_sum += task.workload
            else:
                unfinished_orders += 1
                unfinished_orders_workload_sum += task.workload
        return (
            finished_orders,
            unfinished_orders,
            finished_workload_sum,
            unfinished_orders_workload_sum,
        )


class OrderBookApplication:
    def __init__(self):
        self.do_the_work = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        try:
            programmer, workload = input("programmer and workload estimate: ").split()
            self.do_the_work.add_order(description, programmer, int(workload))
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished_task(self):
        if self.do_the_work.finished_orders():
            for order in self.do_the_work.finished_orders():
                print(order)
        else:
            print("no finished tasks")

    def list_unfinished_task(self):
        if self.do_the_work.unfinished_orders():
            for order in self.do_the_work.unfinished_orders():
                print(order)
        else:
            print("no unfinished tasks")

    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.do_the_work.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def programmers(self):
        names = self.do_the_work.programmers()
        for name in names:
            print(name)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            finished, not_finished, finished_hours, not_finished_hours = (
                self.do_the_work.status_of_programmer(programmer)
            )
            print(
                f"tasks: finished {finished} not finished {not_finished}, hours: done {finished_hours} scheduled {not_finished_hours}"
            )
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_task()
            elif command == "3":
                self.list_unfinished_task()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()


OrderBookApplication().execute()
