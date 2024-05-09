import random

choice = 0
name = 0
point = 0

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0 
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0

ans1 = num1 + num2
ans2 = num3 - num4
ans3 = num5 * num6
ans4 = num7 / num8
ans5 = num9 ** num10



name = input('Hi! What is your name? ')
print('''
###################
Menu
1) Take the quiz
2) View results
3)    Quit
###################
''')
choice = int(input(f'hi {name}, what would you like to do: ' ))

while choice == 1:
    ans1 = int(input(f'Ok, here is the first question \n what is {num1} + {num2}?\n'))
    if ans1 == num1 + num2:
        print('Correct!')
        point = point + 1
        ans2 = int(input(f'ok, here is the next question.\n What is {num3} - {num4}\n '))
        if ans2 == num3 - num4:
            print('Correct!')
            point = point + 1
            ans3 = int(input(f'ok, here is the third question.\n what is {num5} * {num6}\n '))
            if ans3 == num5 * num6:
                print('Correct')
                point = point + 1
                ans4 = int(input(f'Almost there! here is the fourth question.\n what is {num7} / {num8}?\n'))
                if ans4 == num7 / num8:
                    print('Correct')
                    point = point + 1
                    ans5 = int(input(f'Last Question! \n what is {num9}^{num10}?\n'))
                    if ans5 == num9 ** num10:
                        print('Correct!')
                        point = point + 1
                        choice = input('you have completed the quiz. What would you like to do now? ')
                    else print('Wrong')

while choice == 2:
    dd

if choice == 3:
    print(f'Ok {name}, have a nice day!')