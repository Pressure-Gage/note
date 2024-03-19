import math

tim_num = 0
cost = 0
large_box_cost = 6.19
med_box_cost = 3.39
small_box_cost = 1.99
one_tim_cost = 0.20
large_box_amount = 0
med_box_amount = 0
small_box_amount = 0
one_tim_amount = 0


tim_num =  x
while tim_num // 40:
    x = x - 40
    large_box_amount = large_box_amount + 1

while x // 20:
    x = x - 20
    med_box_amount = med_box_amount + 1

while x // 10:
    x = x - 10
    small_box_amount = small_box_amount + 1

while x // 1:
    x = x - 1
    one_tim_amount = one_tim_amount + 1

print("large =", large_box_amount, ", med =", med_box_amount, ", small =", small_box_amount, ", single =", one_tim_amount )
print("that will cost", cost, "$")


