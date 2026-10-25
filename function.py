def check_password(password) :
    if len(password ) <6 :
        return "Too  short"

    print("Password meet length requirement")
    return "Valid Password"

result= check_password("123456")
print(result)