def draw_border(func):
    def wrapper(message):

        print("************************************")
        result= func(message)
        print("******************************")
        return result

    


    return wrapper

@draw_border
def announce(message):
    print(f"System Update Completed : {message}")


announce("Version 2.0 is installed")

announce("Version 3.0 is installed ")

announce("System crashed")

announce("Downloading....")
