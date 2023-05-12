class Worker:

    def __init__(self, name, salary, years_of_work):
        self.name = name
        self.salary = salary
        self.years_of_work = years_of_work

    def getname(self):
        return self.name

    def pension(self):
        return self.years_of_work * (self.salary * 0.1)

    def __str__(self) -> str:
        return self.name + " " + str(self.salary) + " " + \
            str(self.years_of_work) + " " + str(self.pension())


class Manager(Worker):

    def __init__(self, name, salary, years_of_work):
        super().__init__(name, salary, years_of_work)

    def pension(self):
        return self.years_of_work * (self.salary * 0.2)


class Executive(Manager):

    def __init__(self, name, salary, years_of_work):
        super().__init__(name, salary, years_of_work)

    def pension(self):
        return self.years_of_work * (self.salary * 0.3)
