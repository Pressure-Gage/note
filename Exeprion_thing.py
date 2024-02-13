try:
    a = int(input("type a number: "))
    b = int(input("type a second number: "))
    
    print(a/b)

except(ValueError,ZeroDivisionError):
    print("not a valid entry")
    