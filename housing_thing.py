ans = input("do you want to buy a house? ").lower()


if ans == 'yes':
    bedrooms = int(input("how many bedrooms do you want? "))
    if bedrooms <3:
        bathrooms = int(input("how many bathrooms do you want? "))
        print("you have selected", bedrooms, "bedrooms and", bathrooms, " bathrooms")
    elif bedrooms >=3:
        square_feet = int(input("how much square footage are you looking for? "))
    print("you have selected", bedrooms, "bedrooms, and", square_feet, "square feet")
else:
    print("Ok, have a nice day!")