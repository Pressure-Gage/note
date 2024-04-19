choice = 0
student_name = 0
try:
    while choice !=3:
        print('''
        #################
        1. add grades

        2. check grades

            3. exit
        #################
        
        ''')
        choice = int(input("what do you want to do?: "))
        if choice == 1:
            total_students = int(input("how many students are in the class?: "))
            assignment_total = int(input("what is the assignment out of?: "))

            grades = []
            students = []

            while len(students) != total_students:
                add_item = input('enter student name: ')
                students.append(add_item)
                print(students)
                add_item1 = int(input("what is their grade?: "))
                if add_item1 < 0 or add_item1 > assignment_total:
                    add_item1=int(input("that grade isnt possible, reenter grade: "))
                grades.append(add_item1)
                
            print(students)
            print(grades)
        if choice == 2:
            student_name = input("whos grade do you want to see?: ")
            if student_name in students:
                index = student_name.index(student_name)
                print(f"{student_name}'s percentage: {grades[index]}%")
    print("Ok, Goodbye")
except(ValueError,ZeroDivisionError):
    print("not a valid entry")

