import random
numbers = []
total_2 = 0
total = 0
for i in range(1000):
    num = random.randint(1,20)
    total += num
    numbers.append (num)
total_2 = sum(numbers)
print (numbers)
print(len(numbers))
print (total_2)
print (total)

to_ten = []

for i in (numbers):
    if i <=10:
        to_ten.append(i)

print()
print (to_ten)