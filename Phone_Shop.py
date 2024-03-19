try:
    money = 0
    storage = 0
    package = 0
    extra_cloud_storage = 0
    extra_storage = 0
    print('''
    1. McBasic Package
       (50$, 2GB)

    2. Average Joe Package
       (150$, 8GB)

    3. Rich Kid Pro Package
       (800$, 32GB)
    
    ''')
    package = input("what package would you like?: ").lower()

    while package != "mcbasic package" or package != "average joe package" or package != "rich kid pro package" :

        if package == "mcbasic package":
            
            money = money + 50
            storage = storage + 2
            extra_storage = input("would you like extra storage with that? ").lower()
            while extra_storage != "no" or extra_storage != "yes"
                if extra_storage == "no":
                    extra_cloud_storage = input("ok. would you like extra cloud storage? ").lower()
                    if extra_cloud_storage == "no":
                        case = input("would you like a protective case? ").lower()
                        if case == "no":
                            input("ok. would you like an extra fast charger? ").lower()

            break
            

        elif package == "average joe package":
            money = money + 150
            storage = storage + 8
            print (" ok ok")
            extra_storage = input("would you like extra storage with that? ")
            break

        elif package == "rich kid pro package":
            
            money = money + 800
            storage = storage + 32
            print ("ok ok ok")
            extra_storage = input("would you like extra storage with that? ")
            break

        else:
            print ("thats not one of the packages we sell")
            package = input("what package would you like?: ").lower()
    
except(ValueError,ZeroDivisionError):
    print("not a valid entry")