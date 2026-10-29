class CofeeMachine :

    def __init__(self):
        self.__waterlevel = 100
        self.__beanslevel = 50

    def __boil_water(self):
        return "Water boiled to 95°C"

    def __grind_bean(self):
        return "Beans ground to fine poweder"

    def __brew(self):
        return "Hot water pushed through  cofee grounds "

    def make_cofee(self):
        self.__boil_water()
        self.__grind_bean()
        self.__brew()
        return "your Espresso  is ready....!"


my_machine = CofeeMachine()

print(my_machine.make_cofee())

