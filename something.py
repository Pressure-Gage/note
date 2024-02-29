#functions

#define a function

def add_it (x,y):
    return x + y

ans = add_it(3,4)
print (ans)

ans2 = add_it(5,6)
ans3 = add_it(7,8)

#define a function that determines if a number is even or odd

def even_odd(x):
    if x  %2 == 0:
        return 'Even'
    if x%2 !=0:
        return 'Odd'

num_1 = even_odd(8)
print(num_1)
num_2 = even_odd(9)
print(num_2)
