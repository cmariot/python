from random import randint
from time import time
from time import sleep
from os import environ


def log(function):
    """
    This is a decorator that logs into a file called machine.log :
        - the time of execution of a function
        - the user who executed it
        - the name of the function
    """

    def inner(*args, **kwargs):

        user = environ.get('USER') or "anonymous"

        function_name = function.__name__.replace('_', ' ').title()
        if len(function_name) > 20:
            function_name = function_name[:17] + '...'

        start = time()
        ret = function(*args, **kwargs)
        exec_time = time() - start

        if exec_time > 1:
            exec_time = "{:.3f} s ".format(exec_time)
        else:
            exec_time = "{:.3f} ms".format(exec_time * 1000)

        with open("machine.log", "a") as f:
            f.write(
                "({})Running: {:20} [ exec-time = {} ]\n"
                .format(user, function_name, exec_time))
        f.close()
        return ret

    return inner


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_waAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAter(self, water_level):
        sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_waAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAter(70)
