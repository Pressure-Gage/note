
# working with csv file types(comma seperated value)

#file = open('snacks.csv', 'w')
#file.close
import csv
num_inputs = int(input('how many snacks do you want to add?: '))
for i in range (num_inputs):
    file = open('snacks.csv', 'a')
    name = input('enter name of snack: ')
    brand = input('enter the snack brand: ')
    yr_created = int(input('enter the year created: '))
    #when adding files to a csv, they mmust be a string value
    new_record = name + ',' + brand + ',' + str(yr_created) + '\n'
    file.write(str(new_record))
    file.close()

file = open('snacks.csv', 'r')
for i in file:
    print (i)

file.close()
#open from database and save to a list in python
file = open('snacks.csv', 'r')

reader = csv.reader(file)
print (reader)

snacks = list(reader)

print (snacks)