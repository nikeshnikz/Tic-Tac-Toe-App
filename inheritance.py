class Animal :
    def make_sound(slef) :
        print("Some Generic Sound")

class Dog(Animal):

    def make_sound(slef):
        print("woof,woof")


class Cat(Animal):

    def make_sound(slef):
        print("Meow, Moew")

dog = Dog()
cat = Cat()

dog.make_sound()

cat.make_sound()