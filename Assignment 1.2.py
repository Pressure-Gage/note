Balance = int(input("what is your bank balance: "))
payment = Balance * 0.021

if payment >=10:
    print ("you have to pay", payment, "dollars")
elif Balance <10:
     print ("you have to pay", Balance, "dollars")
elif payment <=10:
    print ("you have to pay 10 dollars")