import math

ans = "yes"
while ans == "yes":
    user_ans = int(input('''what would you like to solve:
    1) Area of Rectangle
    2) Times Tables
    3) Exit
    '''))
    if user_ans == 1:
        width = int(input("What is the width of the rectangle?: "))
        height = int(input("What is the height?: "))
        area = width * height
        print (area)
        ans = input("do you want to solve something else? ").lower()
    if user_ans == 2:
        count = 1 
        num = int(input ("give me a number: "))
    while count <13:
        print(count, "times", num, "=", count * num )
        count = count + 1
    ans = input("do you want to solve something else? ").lower()
    if user_ans == 3:
     ans = "no"
    if ans == "no":
        print("ok! Have a nice day")