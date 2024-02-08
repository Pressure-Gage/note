x = int(input("give me a number "))
y = int(input("give me another number "))
z = (input("would you like to Add or Subtract your numbers "))

if z == "Add" or z == "add":
    add = (x + y)
    print ('that would be ', add)

elif z == "subtract" or z == "Subtract":
    sub = (x - y)
    print ('That would be ', sub)

else:
    print("invalid response")