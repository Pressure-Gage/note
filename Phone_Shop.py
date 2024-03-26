try:
    money = 0
    monthly = 0
    storage = 0
    package = 0
    extra_cloud_storage = 0
    extra_storage = 0
    fast_charger = 0
    trade_in = 0
    insurance = 0
    case_type = 0
    case = 0
    data = 0
    data_type = 0
    case_type = 0

    trade_in = input("are you trading in a phone? ").lower()
    while trade_in != "no" and trade_in != "yes":
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
            case = input("would you like a case with that? ").lower()
            while case == "no" or case == "yes":
                if case == "no":
                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                    while fast_charger != "no" or fast_charger != "yes":
                        if fast_charger == "no":
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
            while extra_storage == "no" or extra_storage == "yes":
                if extra_storage == "no":
                    extra_cloud_storage = input("Ok, would you like extra cloud storage? ").lower()
                    while extra_cloud_storage == "no" or extra_cloud_storage == "yes":
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
                    while extra_cloud_storage == "no" or extra_cloud_storage == "yes":
                        if extra_cloud_storage == "no":
                            case = input("Ok, would you like a protective case? ").lower()
                            while case == "no" or case == "yes":
                                if case == "no":
                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                    while fast_charger == "no" or fast_charger == "yes":
                                        if fast_charger == "no":
                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                            while insurance == "no" or insurance == "yes":
                                                if insurance == "no":
                                                    data = input("Ok, would you like a data package? ").lower()
                                                    while data == "no" or data == "yes":
                                                        if data == "no":
                                                            print ("OK, your total comes to", money, "dollars")
                                                            break

                                                        if data == "yes":
                                                            print ('''
                                                            ####################
                                                            
                                                            pay as you go ($0)
                                                            1GB ($10 monthly)
                                                            2GB ($15 monthly)
                                                            5GB ($40 monthly)
                                                            20GB ($150 monthly)

                                                            ####################
                                                            ''')
                                                            data_type = input("what plan would you like? ").lower()
                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                if data_type == "pay as you go":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "1gb":
                                                                    monthly = monthly + 10
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "2gb":
                                                                    monthly = monthly + 15
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "5gb":
                                                                    monthly = monthly + 40
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "20gb":
                                                                    monthly = monthly + 150
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                    
                                                if insurance == "yes":
                                                    monthly = monthly + 1
                                                    data = input("Ok, would you like a data package? ").lower()
                                                    while data == "no" or data == "yes":
                                                        if data == "no":
                                                            print ("OK, your total comes to", money, "dollars")
                                                            break

                                                        if data == "yes":
                                                            print ('''
                                                            ####################
                                                            
                                                            pay as you go ($0)
                                                            1GB ($10 monthly)
                                                            2GB ($15 monthly)
                                                            5GB ($40 monthly)
                                                            20GB ($150 monthly)

                                                            ####################
                                                            ''')
                                                            data_type = input("what plan would you like? ").lower()
                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                if data_type == "pay as you go":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "1gb":
                                                                    monthly = monthly + 10
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "2gb":
                                                                    monthly = monthly + 15
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "5gb":
                                                                    monthly = monthly + 40
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data_type == "20gb":
                                                                    monthly = monthly + 150
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                            if fast_charger == "yes":
                                                money = money + 100
                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                while insurance == "no" or insurance == "yes":
                                                    if insurance == "no":
                                                        data = input("Ok, would you like a data package? ").lower()
                                                        while data == "no" or data == "yes":
                                                            if data == "no":
                                                                print ("OK, your total comes to", money, "dollars")
                                                                break

                                                            if data == "yes":
                                                                print ('''
                                                                ####################
                                                                
                                                                pay as you go ($0)
                                                                1GB ($10 monthly)
                                                                2GB ($15 monthly)
                                                                5GB ($40 monthly)
                                                                20GB ($150 monthly)

                                                                ####################
                                                                ''')
                                                                data_type = input("what plan would you like? ").lower()
                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                    if data_type == "pay as you go":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "1gb":
                                                                        monthly = monthly + 10
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "2gb":
                                                                        monthly = monthly + 15
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "5gb":
                                                                        monthly = monthly + 40
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "20gb":
                                                                        monthly = monthly + 150
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                    if insurance == "yes":
                                                        monthly = monthly + 1
                                                        data = input("Ok, would you like a data package? ").lower()
                                                        while data == "no" or data == "yes":
                                                            if data == "no":
                                                                print ("OK, your total comes to", money, "dollars")
                                                                break

                                                            if data == "yes":
                                                                print ('''
                                                                ####################
                                                                
                                                                pay as you go ($0)
                                                                1GB ($10 monthly)
                                                                2GB ($15 monthly)
                                                                5GB ($40 monthly)
                                                                20GB ($150 monthly)

                                                                ####################
                                                                ''')
                                                                data_type = input("what plan would you like? ").lower()
                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                    if data_type == "pay as you go":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "1gb":
                                                                        monthly = monthly + 10
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "2gb":
                                                                        monthly = monthly + 15
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "5gb":
                                                                        monthly = monthly + 40
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "20gb":
                                                                        monthly = monthly + 150
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break
                                
                                if case == "yes":
                                    print (''' 
                                    ###############
                                    
                                    Rubber ($20)
                                    Carbon fibre ($100)

                                    ###############
                                    ''')
                                    case_type = input("what kind of case do you want?").lower()
                                    while case_type == "rubber" or case_type == "Carbon fibre":
                                        if case_type == "rubber":
                                            money = money + 20
                                            fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                            while fast_charger == "no" or fast_charger == "yes":
                                                if fast_charger == "no":
                                                    insurance = input("Ok, would you like an insurance package? ").lower()
                                                    while insurance == "no" or insurance == "yes":
                                                        if insurance == "no":
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                    
                                                    if insurance == "yes":
                                                        monthly = monthly + 1
                                                        data = input("Ok, would you like a data package? ").lower()
                                                        while data == "no" or data == "yes":
                                                            if data == "no":
                                                                print ("OK, your total comes to", money, "dollars")
                                                                break

                                                            if data == "yes":
                                                                print ('''
                                                                ####################
                                                                
                                                                pay as you go ($0)
                                                                1GB ($10 monthly)
                                                                2GB ($15 monthly)
                                                                5GB ($40 monthly)
                                                                20GB ($150 monthly)

                                                                ####################
                                                                ''')
                                                                data_type = input("what plan would you like? ").lower()
                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                    if data_type == "pay as you go":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "1gb":
                                                                        monthly = monthly + 10
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "2gb":
                                                                        monthly = monthly + 15
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "5gb":
                                                                        monthly = monthly + 40
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "20gb":
                                                                        monthly = monthly + 150
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                    if fast_charger == "yes":
                                                        money = money + 100
                                                        insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                            if insurance == "yes":
                                                                monthly = monthly + 1
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break
                                        
                                        if case_type == "carbon fibre":
                                            money = money + 100
                                            fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                            while fast_charger == "no" or fast_charger == "yes":
                                                if fast_charger == "no":
                                                    insurance = input("Ok, would you like an insurance package? ").lower()
                                                    while insurance == "no" or insurance == "yes":
                                                        if insurance == "no":
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                    
                                                    if insurance == "yes":
                                                        monthly = monthly + 1
                                                        data = input("Ok, would you like a data package? ").lower()
                                                        while data == "no" or data == "yes":
                                                            if data == "no":
                                                                print ("OK, your total comes to", money, "dollars")
                                                                break

                                                            if data == "yes":
                                                                print ('''
                                                                ####################
                                                                
                                                                pay as you go ($0)
                                                                1GB ($10 monthly)
                                                                2GB ($15 monthly)
                                                                5GB ($40 monthly)
                                                                20GB ($150 monthly)

                                                                ####################
                                                                ''')
                                                                data_type = input("what plan would you like? ").lower()
                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                    if data_type == "pay as you go":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "1gb":
                                                                        monthly = monthly + 10
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "2gb":
                                                                        monthly = monthly + 15
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "5gb":
                                                                        monthly = monthly + 40
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data_type == "20gb":
                                                                        monthly = monthly + 150
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                if fast_charger == "yes":
                                                    money = money + 100
                                                    insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                    while insurance == "no" or insurance == "yes":
                                                        if insurance == "no":
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                        if extra_cloud_storage == "yes":
                            print ('''
                                ###############
                                
                                1 Year ($20)
                                2 Years ($35)

                                ###############
                                ''')
                            add_cloud = input("how much cloud backup do you want? ").lower()
                            if add_cloud == "1 year":
                                money = money + 20
                                case = input("Ok, would you like a protective case? ").lower()
                                while case == "no" or case == "yes":
                                    if case == "no":
                                        fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                        while fast_charger == "no" or fast_charger == "yes":
                                                    if fast_charger == "no":
                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                            
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                        
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                        ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                        if fast_charger == "yes":
                                                            money = money + 100
                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                                
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break
                                    
                                    if case == "yes":
                                        print (''' 
                                        ###############
                                        
                                        Rubber ($20)
                                        Carbon fibre ($100)

                                        ###############
                                        ''')
                                        case_type = input("what kind of case do you want?").lower()
                                        while case_type == "rubber" or case_type == "Carbon fibre":
                                            if case_type == "rubber":
                                                money = money + 20
                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                while fast_charger == "no" or fast_charger == "yes":
                                                    if fast_charger == "no":
                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                        
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                        if fast_charger == "yes":
                                                            money = money + 100
                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break
                                            
                                            if case_type == "carbon fibre":
                                                money = money + 100
                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                while fast_charger == "no" or fast_charger == "yes":
                                                    if fast_charger == "no":
                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                        
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                        if fast_charger == "yes":
                                                            money = money + 100
                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break
                                if add_cloud == "2 Years":
                                    money = money + 35
                                    case = input("Ok, would you like a protective case? ").lower()
                                    while case == "no" or case == "yes":  
                                        if case == "no":
                                            fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                            while fast_charger == "no" or fast_charger == "yes":
                                                if fast_charger == "no":
                                                    insurance = input("Ok, would you like an insurance package? ").lower()
                                                    while insurance == "no" or insurance == "yes":
                                                        if insurance == "no":
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                            
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                    if fast_charger == "yes":
                                                        money = money + 100
                                                        insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                            if insurance == "yes":
                                                                monthly = monthly + 1
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break
                                        
                                        if case == "yes":
                                            print (''' 
                                            ###############
                                            
                                            Rubber ($20)
                                            Carbon fibre ($100)

                                            ###############
                                            ''')
                                            case_type = input("what kind of case do you want?").lower()
                                            while case_type == "rubber" or case_type == "Carbon fibre":
                                                if case_type == "rubber":
                                                    money = money + 20
                                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                    while fast_charger == "no" or fast_charger == "yes":
                                                        if fast_charger == "no":
                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                            
                                                            if insurance == "yes":
                                                                monthly = monthly + 1
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                            if fast_charger == "yes":
                                                                money = money + 100
                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                while insurance == "no" or insurance == "yes":
                                                                    if insurance == "no":
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                    if insurance == "yes":
                                                                        monthly = monthly + 1
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break
                                                
                                                if case_type == "carbon fibre":
                                                    money = money + 100
                                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                    while fast_charger == "no" or fast_charger == "yes":
                                                        if fast_charger == "no":
                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                            
                                                            if insurance == "yes":
                                                                monthly = monthly + 1
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                            if fast_charger == "yes":
                                                                money = money + 100
                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                while insurance == "no" or insurance == "yes":
                                                                    if insurance == "no":
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                    if insurance == "yes":
                                                                        monthly = monthly + 1
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                    

            if extra_storage == "yes":
                print(''' 
                ##############################

                    Additional 64GB ($200)
                    Additional 128GB ($350)

                ##############################''')
                add_storage = input("How much additional storage would you like? ").lower()
                while add_storage != "64gb" or add_storage != "128gb":
                    if add_storage == "64gb":
                        money = money + 200
                        extra_cloud_storage = input("Ok, would you like extra cloud storage? ").lower()
                        while extra_cloud_storage == "no" or extra_cloud_storage == "yes":
                            if extra_cloud_storage == "no":
                                case = input("Ok, would you like a protective case? ").lower()
                                while case == "no" or case == "yes":
                                    if case == "no":
                                        fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                        while fast_charger == "no" or fast_charger == "yes":
                                                    if fast_charger == "no":
                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                        
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                        if fast_charger == "yes":
                                                            money = money + 100
                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break
                                    
                                    if case == "yes":
                                        print (''' 
                                        ###############
                                        
                                        Rubber ($20)
                                        Carbon fibre ($100)

                                        ###############
                                        ''')
                                        case_type = input("what kind of case do you want?").lower()
                                        while case_type == "rubber" or case_type == "Carbon fibre":
                                            if case_type == "rubber":
                                                money = money + 20
                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                while fast_charger == "no" or fast_charger == "yes":
                                                    if fast_charger == "no":
                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                        
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                        if fast_charger == "yes":
                                                            money = money + 100
                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                            while insurance == "no" or insurance == "yes":
                                                                if insurance == "no":
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break
                                            
                                            if case_type == "carbon fibre":
                                                money = money + 100
                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                while fast_charger == "no" or fast_charger == "yes":
                                                    if fast_charger == "no":
                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                        
                                                        if insurance == "yes":
                                                            monthly = monthly + 1
                                                            data = input("Ok, would you like a data package? ").lower()
                                                            while data == "no" or data == "yes":
                                                                if data == "no":
                                                                    print ("OK, your total comes to", money, "dollars")
                                                                    break

                                                                if data == "yes":
                                                                    print ('''
                                                                    ####################
                                                                    
                                                                    pay as you go ($0)
                                                                    1GB ($10 monthly)
                                                                    2GB ($15 monthly)
                                                                    5GB ($40 monthly)
                                                                    20GB ($150 monthly)

                                                                    ####################
                                                                    ''')
                                                                    data_type = input("what plan would you like? ").lower()
                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                        if data_type == "pay as you go":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "1gb":
                                                                            monthly = monthly + 10
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "2gb":
                                                                            monthly = monthly + 15
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "5gb":
                                                                            monthly = monthly + 40
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data_type == "20gb":
                                                                            monthly = monthly + 150
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                    if fast_charger == "yes":
                                                        money = money + 100
                                                        insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                        while insurance == "no" or insurance == "yes":
                                                            if insurance == "no":
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                            if insurance == "yes":
                                                                monthly = monthly + 1
                                                                data = input("Ok, would you like a data package? ").lower()
                                                                while data == "no" or data == "yes":
                                                                    if data == "no":
                                                                        print ("OK, your total comes to", money, "dollars")
                                                                        break

                                                                    if data == "yes":
                                                                        print ('''
                                                                        ####################
                                                                        
                                                                        pay as you go ($0)
                                                                        1GB ($10 monthly)
                                                                        2GB ($15 monthly)
                                                                        5GB ($40 monthly)
                                                                        20GB ($150 monthly)

                                                                        ####################
                                                                        ''')
                                                                        data_type = input("what plan would you like? ").lower()
                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                            if data_type == "pay as you go":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "1gb":
                                                                                monthly = monthly + 10
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "2gb":
                                                                                monthly = monthly + 15
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "5gb":
                                                                                monthly = monthly + 40
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data_type == "20gb":
                                                                                monthly = monthly + 150
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                        if extra_cloud_storage == "yes":
                                            print ('''
                                            ###############
                                            
                                            1 Year ($20)
                                            2 Years ($35)

                                            ###############
                                            ''')
                                            add_cloud = input("how much cloud backup do you want? ").lower()
                                            if add_cloud == "1 year":
                                                money = money + 20
                                                case = input("Ok, would you like a protective case? ").lower()
                                                while case == "no" or case == "yes":
                                                    if case == "no":
                                                        fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                        while fast_charger == "no" or fast_charger == "yes":
                                                                    if fast_charger == "no":
                                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                                        while insurance == "no" or insurance == "yes":
                                                                            if insurance == "no":
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                        
                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if fast_charger == "yes":
                                                                            money = money + 100
                                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                if insurance == "yes":
                                                                                    monthly = monthly + 1
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break
                                                    
                                                    if case == "yes":
                                                        print (''' 
                                                        ###############
                                                        
                                                        Rubber ($20)
                                                        Carbon fibre ($100)

                                                        ###############
                                                        ''')
                                                        case_type = input("what kind of case do you want?").lower()
                                                        while case_type == "rubber" or case_type == "Carbon fibre":
                                                            if case_type == "rubber":
                                                                money = money + 20
                                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                while fast_charger == "no" or fast_charger == "yes":
                                                                    if fast_charger == "no":
                                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                                        while insurance == "no" or insurance == "yes":
                                                                            if insurance == "no":
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                        
                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if fast_charger == "yes":
                                                                            money = money + 100
                                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                if insurance == "yes":
                                                                                    monthly = monthly + 1
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break
                                                            
                                                            if case_type == "carbon fibre":
                                                                money = money + 100
                                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                while fast_charger == "no" or fast_charger == "yes":
                                                                    if fast_charger == "no":
                                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                                        while insurance == "no" or insurance == "yes":
                                                                            if insurance == "no":
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                        
                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if fast_charger == "yes":
                                                                            money = money + 100
                                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                if insurance == "yes":
                                                                                    monthly = monthly + 1
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break
                                                if add_cloud == "2 Years":
                                                    money = money + 35
                                                    case = input("Ok, would you like a protective case? ").lower()
                                                    while case == "no" or case == "yes":  
                                                        if case == "no":
                                                            fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                            while fast_charger == "no" or fast_charger == "yes":
                                                                        if fast_charger == "no":
                                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                            
                                                                            if insurance == "yes":
                                                                                monthly = monthly + 1
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                            if fast_charger == "yes":
                                                                                money = money + 100
                                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                                while insurance == "no" or insurance == "yes":
                                                                                    if insurance == "no":
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                    if insurance == "yes":
                                                                                        monthly = monthly + 1
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break
                                                        
                                                        if case == "yes":
                                                            print (''' 
                                                            ###############
                                                            
                                                            Rubber ($20)
                                                            Carbon fibre ($100)

                                                            ###############
                                                            ''')
                                                            case_type = input("what kind of case do you want?").lower()
                                                            while case_type == "rubber" or case_type == "Carbon fibre":
                                                                if case_type == "rubber":
                                                                    money = money + 20
                                                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                    while fast_charger == "no" or fast_charger == "yes":
                                                                        if fast_charger == "no":
                                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                            
                                                                            if insurance == "yes":
                                                                                monthly = monthly + 1
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                            if fast_charger == "yes":
                                                                                money = money + 100
                                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                                while insurance == "no" or insurance == "yes":
                                                                                    if insurance == "no":
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                    if insurance == "yes":
                                                                                        monthly = monthly + 1
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break
                                                                
                                                                if case_type == "carbon fibre":
                                                                    money = money + 100
                                                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                    while fast_charger == "no" or fast_charger == "yes":
                                                                        if fast_charger == "no":
                                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                            
                                                                            if insurance == "yes":
                                                                                monthly = monthly + 1
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                            if fast_charger == "yes":
                                                                                money = money + 100
                                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                                while insurance == "no" or insurance == "yes":
                                                                                    if insurance == "no":
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                    if insurance == "yes":
                                                                                        monthly = monthly + 1
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                    print ("thant is not an option")
                                                    print ('''
                                                    ###############
                                                    
                                                    1 Year ($20)
                                                    2 Years ($35)

                                                    ############### ''')
                                                    add_cloud = input("how much cloud backup do you want? ").lower()
                                

                            if add_storage == "128gb":
                                money = money + 350
                                extra_cloud_storage = input("Ok, would you like extra cloud storage? ").lower()
                                while extra_cloud_storage == "no" or extra_cloud_storage == "yes":
                                    if extra_cloud_storage == "no":
                                        case = input("Ok, would you like a protective case? ").lower()
                                        while case == "no" or case == "yes":
                                            if case == "no":
                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                while fast_charger == "no" or fast_charger == "yes":
                                                            if fast_charger == "no":
                                                                insurance = input("Ok, would you like an insurance package? ").lower()
                                                                while insurance == "no" or insurance == "yes":
                                                                    if insurance == "no":
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                
                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if fast_charger == "yes":
                                                                    money = money + 100
                                                                    insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                    while insurance == "no" or insurance == "yes":
                                                                        if insurance == "no":
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break
                                            
                                            if case == "yes":
                                                print (''' 
                                                ###############
                                                
                                                Rubber ($20)
                                                Carbon fibre ($100)

                                                ###############
                                                ''')
                                                case_type = input("what kind of case do you want?").lower()
                                                while case_type == "rubber" or case_type == "Carbon fibre":
                                                    if case_type == "rubber":
                                                        money = money + 20
                                                        fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                        while fast_charger == "no" or fast_charger == "yes":
                                                            if fast_charger == "no":
                                                                insurance = input("Ok, would you like an insurance package? ").lower()
                                                                while insurance == "no" or insurance == "yes":
                                                                    if insurance == "no":
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                
                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                if fast_charger == "yes":
                                                                    money = money + 100
                                                                    insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                    while insurance == "no" or insurance == "yes":
                                                                        if insurance == "no":
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break
                                                    
                                                    if case_type == "carbon fibre":
                                                        money = money + 100
                                                        fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                        while fast_charger == "no" or fast_charger == "yes":
                                                            if fast_charger == "no":
                                                                insurance = input("Ok, would you like an insurance package? ").lower()
                                                                while insurance == "no" or insurance == "yes":
                                                                    if insurance == "no":
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                
                                                                if insurance == "yes":
                                                                    monthly = monthly + 1
                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                    while data == "no" or data == "yes":
                                                                        if data == "no":
                                                                            print ("OK, your total comes to", money, "dollars")
                                                                            break

                                                                        if data == "yes":
                                                                            print ('''
                                                                            ####################
                                                                            
                                                                            pay as you go ($0)
                                                                            1GB ($10 monthly)
                                                                            2GB ($15 monthly)
                                                                            5GB ($40 monthly)
                                                                            20GB ($150 monthly)

                                                                            ####################
                                                                            ''')
                                                                            data_type = input("what plan would you like? ").lower()
                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                if data_type == "pay as you go":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "1gb":
                                                                                    monthly = monthly + 10
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "2gb":
                                                                                    monthly = monthly + 15
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "5gb":
                                                                                    monthly = monthly + 40
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data_type == "20gb":
                                                                                    monthly = monthly + 150
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                            if fast_charger == "yes":
                                                                money = money + 100
                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                while insurance == "no" or insurance == "yes":
                                                                    if insurance == "no":
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                    if insurance == "yes":
                                                                        monthly = monthly + 1
                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                        while data == "no" or data == "yes":
                                                                            if data == "no":
                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                break

                                                                            if data == "yes":
                                                                                print ('''
                                                                                ####################
                                                                                
                                                                                pay as you go ($0)
                                                                                1GB ($10 monthly)
                                                                                2GB ($15 monthly)
                                                                                5GB ($40 monthly)
                                                                                20GB ($150 monthly)

                                                                                ####################
                                                                                ''')
                                                                                data_type = input("what plan would you like? ").lower()
                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                    if data_type == "pay as you go":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "1gb":
                                                                                        monthly = monthly + 10
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "2gb":
                                                                                        monthly = monthly + 15
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "5gb":
                                                                                        monthly = monthly + 40
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data_type == "20gb":
                                                                                        monthly = monthly + 150
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                        if extra_cloud_storage == "yes":
                                            print ('''
                                            ###############
                                            
                                            1 Year ($20)
                                            2 Years ($35)

                                            ###############
                                            ''')
                                            add_cloud = input("how much cloud backup do you want? ").lower()
                                            if add_cloud == "1 year":
                                                money = money + 20
                                                case = input("Ok, would you like a protective case? ").lower()
                                                while case == "no" or case == "yes":
                                                    if case == "no":
                                                        fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                        while fast_charger == "no" or fast_charger == "yes":
                                                                    if fast_charger == "no":
                                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                                        while insurance == "no" or insurance == "yes":
                                                                            if insurance == "no":
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                        
                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if fast_charger == "yes":
                                                                            money = money + 100
                                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                if insurance == "yes":
                                                                                    monthly = monthly + 1
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break
                                                    
                                                    if case == "yes":
                                                        print (''' 
                                                        ###############
                                                        
                                                        Rubber ($20)
                                                        Carbon fibre ($100)

                                                        ###############
                                                        ''')
                                                        case_type = input("what kind of case do you want?").lower()
                                                        while case_type == "rubber" or case_type == "Carbon fibre":
                                                            if case_type == "rubber":
                                                                money = money + 20
                                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                while fast_charger == "no" or fast_charger == "yes":
                                                                    if fast_charger == "no":
                                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                                        while insurance == "no" or insurance == "yes":
                                                                            if insurance == "no":
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                        
                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if fast_charger == "yes":
                                                                            money = money + 100
                                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                if insurance == "yes":
                                                                                    monthly = monthly + 1
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break
                                                            
                                                            if case_type == "carbon fibre":
                                                                money = money + 100
                                                                fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                while fast_charger == "no" or fast_charger == "yes":
                                                                    if fast_charger == "no":
                                                                        insurance = input("Ok, would you like an insurance package? ").lower()
                                                                        while insurance == "no" or insurance == "yes":
                                                                            if insurance == "no":
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                        
                                                                        if insurance == "yes":
                                                                            monthly = monthly + 1
                                                                            data = input("Ok, would you like a data package? ").lower()
                                                                            while data == "no" or data == "yes":
                                                                                if data == "no":
                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                    break

                                                                                if data == "yes":
                                                                                    print ('''
                                                                                    ####################
                                                                                    
                                                                                    pay as you go ($0)
                                                                                    1GB ($10 monthly)
                                                                                    2GB ($15 monthly)
                                                                                    5GB ($40 monthly)
                                                                                    20GB ($150 monthly)

                                                                                    ####################
                                                                                    ''')
                                                                                    data_type = input("what plan would you like? ").lower()
                                                                                    while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                        if data_type == "pay as you go":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "1gb":
                                                                                            monthly = monthly + 10
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "2gb":
                                                                                            monthly = monthly + 15
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "5gb":
                                                                                            monthly = monthly + 40
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data_type == "20gb":
                                                                                            monthly = monthly + 150
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                        if fast_charger == "yes":
                                                                            money = money + 100
                                                                            insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                if insurance == "yes":
                                                                                    monthly = monthly + 1
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break
                                                if add_cloud == "2 Years":
                                                    money = money + 35
                                                    case = input("Ok, would you like a protective case? ").lower()
                                                    while case == "no" or case == "yes":  
                                                        if case == "no":
                                                            fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                            while fast_charger == "no" or fast_charger == "yes":
                                                                        if fast_charger == "no":
                                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                            
                                                                            if insurance == "yes":
                                                                                monthly = monthly + 1
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                            if fast_charger == "yes":
                                                                                money = money + 100
                                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                                while insurance == "no" or insurance == "yes":
                                                                                    if insurance == "no":
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                    if insurance == "yes":
                                                                                        monthly = monthly + 1
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break
                                                        
                                                        if case == "yes":
                                                            print (''' 
                                                            ###############
                                                            
                                                            Rubber ($20)
                                                            Carbon fibre ($100)

                                                            ###############
                                                            ''')
                                                            case_type = input("what kind of case do you want?").lower()
                                                            while case_type == "rubber" or case_type == "Carbon fibre":
                                                                if case_type == "rubber":
                                                                    money = money + 20
                                                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                    while fast_charger == "no" or fast_charger == "yes":
                                                                        if fast_charger == "no":
                                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                            
                                                                            if insurance == "yes":
                                                                                monthly = monthly + 1
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                            if fast_charger == "yes":
                                                                                money = money + 100
                                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                                while insurance == "no" or insurance == "yes":
                                                                                    if insurance == "no":
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                    if insurance == "yes":
                                                                                        monthly = monthly + 1
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break
                                                                
                                                                if case_type == "carbon fibre":
                                                                    money = money + 100
                                                                    fast_charger = input("Ok, would you like an extra fast charger? ").lower()
                                                                    while fast_charger == "no" or fast_charger == "yes":
                                                                        if fast_charger == "no":
                                                                            insurance = input("Ok, would you like an insurance package? ").lower()
                                                                            while insurance == "no" or insurance == "yes":
                                                                                if insurance == "no":
                                                                                    data = input("Ok, would you like a data package? ").lower()
                                                                                    while data == "no" or data == "yes":
                                                                                        if data == "no":
                                                                                            print ("OK, your total comes to", money, "dollars")
                                                                                            break

                                                                                        if data == "yes":
                                                                                            print ('''
                                                                                            ####################
                                                                                            
                                                                                            pay as you go ($0)
                                                                                            1GB ($10 monthly)
                                                                                            2GB ($15 monthly)
                                                                                            5GB ($40 monthly)
                                                                                            20GB ($150 monthly)

                                                                                            ####################
                                                                                            ''')
                                                                                            data_type = input("what plan would you like? ").lower()
                                                                                            while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                if data_type == "pay as you go":
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "1gb":
                                                                                                    monthly = monthly + 10
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "2gb":
                                                                                                    monthly = monthly + 15
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "5gb":
                                                                                                    monthly = monthly + 40
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                                                if data_type == "20gb":
                                                                                                    monthly = monthly + 150
                                                                                                    print ("OK, your total comes to", money, "dollars")
                                                                                                    break

                                                                            
                                                                            if insurance == "yes":
                                                                                monthly = monthly + 1
                                                                                data = input("Ok, would you like a data package? ").lower()
                                                                                while data == "no" or data == "yes":
                                                                                    if data == "no":
                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                        break

                                                                                    if data == "yes":
                                                                                        print ('''
                                                                                        ####################
                                                                                        
                                                                                        pay as you go ($0)
                                                                                        1GB ($10 monthly)
                                                                                        2GB ($15 monthly)
                                                                                        5GB ($40 monthly)
                                                                                        20GB ($150 monthly)

                                                                                        ####################
                                                                                        ''')
                                                                                        data_type = input("what plan would you like? ").lower()
                                                                                        while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                            if data_type == "pay as you go":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "1gb":
                                                                                                monthly = monthly + 10
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "2gb":
                                                                                                monthly = monthly + 15
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "5gb":
                                                                                                monthly = monthly + 40
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data_type == "20gb":
                                                                                                monthly = monthly + 150
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                            if fast_charger == "yes":
                                                                                money = money + 100
                                                                                insurance = input("Ok, would you like an insurance package for  a month? ").lower()
                                                                                while insurance == "no" or insurance == "yes":
                                                                                    if insurance == "no":
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                    if insurance == "yes":
                                                                                        monthly = monthly + 1
                                                                                        data = input("Ok, would you like a data package? ").lower()
                                                                                        while data == "no" or data == "yes":
                                                                                            if data == "no":
                                                                                                print ("OK, your total comes to", money, "dollars")
                                                                                                break

                                                                                            if data == "yes":
                                                                                                print ('''
                                                                                                ####################
                                                                                                
                                                                                                pay as you go ($0)
                                                                                                1GB ($10 monthly)
                                                                                                2GB ($15 monthly)
                                                                                                5GB ($40 monthly)
                                                                                                20GB ($150 monthly)

                                                                                                ####################
                                                                                                ''')
                                                                                                data_type = input("what plan would you like? ").lower()
                                                                                                while data_type == "pay as you go" or data_type == "1gb" or data_type == "2gb" or data_type == "5gb" or data_type == "20gb":
                                                                                                    if data_type == "pay as you go":
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "1gb":
                                                                                                        monthly = monthly + 10
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "2gb":
                                                                                                        monthly = monthly + 15
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "5gb":
                                                                                                        monthly = monthly + 40
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                                                                    if data_type == "20gb":
                                                                                                        monthly = monthly + 150
                                                                                                        print ("OK, your total comes to", money, "dollars")
                                                                                                        break

                                                    print ("thant is not an option")
                                                    print ('''
                                                    ###############
                                                    
                                                    1 Year ($20)
                                                    2 Years ($35)

                                                    ############### ''')
                                                    add_cloud = input("how much cloud backup do you want? ").lower()


                            print("that in not an option")
                            print(''' 
                            ######################

                                Additional 64GB
                                Additional 128GB

                            ######################''')
                            add_storage = input("How much additional storage would you like? ").lower()
                
                
                if extra_storage == "yes":
                    d
        else:
            print ("thats not one of the packages we sell")
            package = input("what package would you like?: ").lower()
    
except(ValueError,ZeroDivisionError):
    print("not a valid entry")