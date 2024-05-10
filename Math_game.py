import random
import csv

choice = 0
name = 0
point = 0
quiz_results = 0
questions = 5

num1 = 0
num2 = 0


print('''
###################
Menu
1) Take the quiz
2) View results
3)    Quit
###################
''')
choice = int(input(f'hi , what would you like to do: ' ))

if choice == 1:
    file = open('quiz_results.csv', 'a')
    name = input('what is your name? ')
    num1 = random.randint (1,10)
    num2 = random.randint (1,10)
    pans1 = int(input(f'Ok, here is the first question \n what is {num1} + {num2}?\n'))
    if pans1 == num1 + num2:
        print('Correct!')
        point = point + 1
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans2 = int(input(f'ok, here is the next question.\n What is {num1} - {num2}\n '))
    else:
        print('Wrong')
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans2 = int(input(f'ok, here is the next question.\n What is {num1} - {num2}\n '))

    if pans2 == num1 - num2:
        print('Correct!')
        point = point + 1
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans3 = int(input(f'ok, here is the third question.\n what is {num1} * {num2}\n '))
    else:
        print('Wrong')
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans3 = int(input(f'ok, here is the third question.\n what is {num1} * {num2}\n '))          
       
    if pans3 == num1 * num2:
        print('Correct')
        point = point + 1
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans4 = float(input(f'Almost there! here is the fourth question.\n what is {num1} / {num2}?\n'))
    else:
        print('Wrong')
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans4 = int(input(f'Almost there! here is the fourth question.\n what is {num1} / {num2}?\n'))
    
    if pans4 == round((num1 / num2), 2):
        print('Correct')
        point = point + 1
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans5 = int(input(f'Last Question! \n what is {num1}^{num2}?\n'))
    else:
        print('Wrong')
        num1 = random.randint (1,10)
        num2 = random.randint (1,10)
        pans5 = int(input(f'Last Question! \n what is {num1}^{num2}?\n'))
    
    if pans5 == num1 ** num2:
        print('Correct!')
        point = point + 1
        quiz_results = (point / questions) * 100
        new_record = (name) + ',' + str(point) + ',' + str(questions) + ',' + str(quiz_results) + '\n'
        file.write(str(new_record))
        file.close
        choice = int(input('you have completed the quiz. What would you like to do now? '))
    else:
        print('Wrong')
        quiz_results = (point / questions) * 100
        new_record = (name) + ',' + str(point) + ',' + str(questions) + ',' + str(quiz_results) + '\n'
        file.write(str(new_record))
        file.close
        choice = int(input('you have completed the quiz. What would you like to do now? '))





if choice == 2:
    file = open('quiz_results.csv', 'r')
    reader = csv.reader(file)
    Math = list(reader)
    print (Math)
    file.close()
    choice = input('What would you like to do now? ')

if choice == 3:
    print(f'Ok {name}, have a nice day!')
    