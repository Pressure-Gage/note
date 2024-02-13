password = "cheese"

user_name = input("what is your name: ")

user_password = input("what is the password: ")

if user_password == password:
    print("Welcome", user_name)
else:
    print("Invalid Password")