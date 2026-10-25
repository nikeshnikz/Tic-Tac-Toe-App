current_user_role = "admin"
def admin_only(func) :
    def wrapper() :
        if current_user_role != "admin" :
            print("Access Denied : Admin Only")
            return
        return func
    return wrapper

@admin_only
def delete_database():
    print("Database sucessfully deleted")

print("Attempting to delete as 'guest' ")
delete_database()

print("\nSwitching role to 'admin")
current_user_role = "admin"
delete_database()

    