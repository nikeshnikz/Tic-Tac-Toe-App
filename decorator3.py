def make_bold(func) :
    def wrapper(message):
        
        return func(f" <b> {message} </b>")


    return wrapper


@make_bold
def post_title(message):
    return message


print(post_title("Breaking News"))

print(post_title("Welcome Home"))

print(post_title("See you soon"))

@make_bold
def end_credit(message):
    return message

print(end_credit("The End"))

print(end_credit("This is the conclusion"))

print(end_credit("There is no  Credit scene Available"))

print(end_credit("************************************"))

print(end_credit("There is an End Credit  Scene Included "))

