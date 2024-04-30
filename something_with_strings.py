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

# join

words = [
   'the', 'cow', 'jumped', "over", 'the', 'moon'
]
one_word = ' '.join(words)
print (one_word)

#trailing white space
#get rid using .strip

q = '   hello white space     '
stripped = q.strip()
print (stripped)

#finding an index
print ('animals'.index('m'))
print ('animals'.find('m'))  #same as index, dbut no error when not found, where as index will show an error if not found

#in command

x = 'cat' in 'cat in hat' #returns a boolean T/F
y = 'bat' in 'cat in hat'
print (x,y)
#formatting for a new line

print ('Roses are red,\n Violets are blue,\n I like coding,\n how about you?')

#.replace

sentance = 'she is so stupendous'
new_sentance = sentance.replace('s', '$') #looking for, replace with
print(new_sentance)