total_students = int(input("how many students are in the class?: "))
asssignment_total = int(input("what is the assignment out of?: "))


students = []
print (len(students))

while len(students) != total_students:
    add_item = input('enter student name: ')
    students.append(add_item)
    add_item1 = int(input("what is their grade?: "))
    print(students)
grades = []
    