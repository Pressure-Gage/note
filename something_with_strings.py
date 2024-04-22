#you can index strings

author = 'Hemingway'

print(author[0:2]) #start index: end index

#concatenate/ add strings together

author2 = 'Ernest'
full_name = author2 + author
print(full_name)

print(full_name[4:6]+full_name[-2:])
#leaving the end bound open defaults to end of string

# format strings

name = 'josh'
age = 18
color = "blue"
print(f'{name} is {age} years old. there favorite color is {color}')

user = input (f"hello {name} please enter age: ")