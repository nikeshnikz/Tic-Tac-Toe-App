def postive_only(func):
    def wrapper(number) :
        if number < 0 :
            return f"Error: only positive number allowed!"
        if number > 0 :
            pass
        return func(number)


    return wrapper

@postive_only
def sqr_root(number):
    return number ** 0.5

print(sqr_root(25))

print(sqr_root(67))

print(sqr_root(64))