

people = 0

ans = input("do you want to invite someone? ").lower()
while ans == 'yes':
    person = input('who do you want to invite? ')
    print('ok,', person, "has been invited.")
    people +=1
    ans = input("do you want to invite someone else? ").lower()

print("ok, you have invited", people, "people to the party.")