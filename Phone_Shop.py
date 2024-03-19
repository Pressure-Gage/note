try:
    money = 0
    storage = 0
    package = 0
    extra_cloud_storage = 0
    extra_storage = 0
    fast_charger = 0
    trade_in = 0
    insurance = 0
    case_type = 0

    trade_in = input("are you trading in a phone? ").lower()
    while trade_in != "no" or trade_in != "yes":
        if trade_in == "yes":
            money = money + 40
            break
        elif trade_in == "no":
            print ("Ok")
            break
        else:
            print("Thats not a valid answer")
            trade_in = input("are you trading in a phone? ").lower()

    
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
            while case != "no" or case!= "yes":
                if case == "no":
                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                    while fast_charger != "no" or fast_charger != "yes":
                        if fast_charger =="no":
                            insurance = input("Ok, would you like an insurance package? ").lower()
                            while insurance != "no" or insurance != "yes":
                                if insurance == "no":
                                    data = input("Ok, would you like a data package? ").lower()
                                    while data != "no" or data != "yes":
                                        if data == "no":
                                            print ("OK, your total comes to", money, "dollars")
                                            break    
                if case == "yes":
                    case_type = input("Do you want a Rubber Case, or a Carbon Fibre case? ").lower
                    if case_type == "rubber":
                        money = money + 20
            
            break
            

        elif package == "average joe package":
            money = money + 150
            storage = storage + 8
            extra_storage = input("would you like extra storage with that? ").lower()
            while extra_storage != "no" or extra_storage != "yes":
                if extra_storage == "no":
                    extra_cloud_storage = input("Ok, would you like extra cloud storage? ").lower()
                    while extra_cloud_storage != "no" or extra_cloud_storage != "yes":
                        if extra_cloud_storage == "no":
                            case = input("Ok, would you like a protective case? ").lower()
                            while case != "no" or case!= "yes":
                                if case == "no":
                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                    while fast_charger != "no" or fast_charger != "yes":
                                        if fast_charger =="no":
                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                            while insurance != "no" or insurance != "yes":
                                                if insurance == "no":
                                                    data = input("Ok, would you like a data package? ").lower()
                                                    while data != "no" or data != "yes":
                                                        if data == "no":
                                                            print ("OK, your total comes to", money, "dollars")
                                                            break

        elif package == "rich kid pro package":
            
            money = money + 800
            storage = storage + 32
            extra_storage = input("would you like extra storage with that? ").lower()
            while extra_storage != "no" or extra_storage != "yes":
                if extra_storage == "no":
                    extra_cloud_storage = input("Ok, would you like extra cloud storage? ").lower()
                    while extra_cloud_storage != "no" or extra_cloud_storage != "yes":
                        if extra_cloud_storage == "no":
                            case = input("Ok, would you like a protective case? ").lower()
                            while case != "no" or case!= "yes":
                                if case == "no":
                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                    while fast_charger != "no" or fast_charger != "yes":
                                        if fast_charger =="no":
                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                            while insurance != "no" or insurance != "yes":
                                                if insurance == "no":
                                                    data = input("Ok, would you like a data package? ").lower()
                                                    while data != "no" or data != "yes":
                                                        if data == "no":
                                                            print ("OK, your total comes to", money, "dollars")
                                                            break

        else:
            print ("thats not one of the packages we sell")
            package = input("what package would you like?: ").lower()
    
except(ValueError,ZeroDivisionError):
    print("not a valid entry")