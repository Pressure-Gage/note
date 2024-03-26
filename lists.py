#Lists

#how to make a list
#two ways

#1
fruit = list()

#2
fruit = []

fruit = ['Apple', 'Orange', 'Pear', 'Watermelon']

#indexing - accessing an item in the list

print(fruit[1]) #Orange
print (fruit[3]) #watermelon

print(fruit[-3])
print (fruit[-1])

#add an item
add_item = input('enter a fruit: ')
#append
fruit.append(add_item)
#append will always add items to the list
print (fruit)

# lists are mutable
#change n item in the list

fruit[0] = 'Starfruit'

print (fruit)

#length

print (len(fruit))

#removing an item from a list
#remove last item
fruit.pop()

#to remove an item from a list, input the positional integer
fruit.pop(1)

#remove an item by name
fruit.remove('Pear')

