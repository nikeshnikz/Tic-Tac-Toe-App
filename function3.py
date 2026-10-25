def wash_hand(meal_function):
    def routine():
        print("washing hand with soap")
        meal_function()
        print("washing hand and drying with towel")

    return routine  # Aligned with 'def routine()' so wash_hand returns it!


@wash_hand
def eat_pizza():
    print("Eating Delicious Pizza")


# Unindented all the way to the left so it runs:
eat_pizza()

