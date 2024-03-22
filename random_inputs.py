# import random
import random

gen = input("do you want me to generate a random number? ").lower()

while gen == "yes":
    x = random.randint(1, 20) # returns a random integer
    print (x)
    gen = input("do you want me to generate a random number? ").lower()
    if gen != "yes":
        break

print (" thanks for running the program")
# other random functions
a = random.random() # will return a random float pt. between 0 and 1
a = a * 1000
print (a)

# random choice
color = random.choice(['red', 'blue', 'green', 'purple', 'orange']) #set a list
print (color)
