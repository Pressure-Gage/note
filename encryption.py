choice = 0
dict1 = 0
encoded_message = 0
all_encoded_messages = ""
password = 'password'

username = input('what is your name?: ')
print('''
  ####################
   1) Encode Message
   2) Decode Message
  3) See All Messages
       4) Exit
  ####################
''')
choice = int(input(f'hello {username}, what would you like to do?: '))
if choice == 1:
  message = input('what do you want to be encoded?: ')
  encoded_message = ""
  for i in range (len(message)):
    encoded_message = encoded_message + chr(ord(message[i]) + 3)
  print (encoded_message)
  all_encoded_messages.append(encoded_message)

if choice == 2:
  input_password = input('what is the password').lower()
  while input_password != 'password':
    input_password = ('invalid password, try again: ')
  decode = int(input(f'ok {username}, what would you like to decode?: '))
  decoded_message = ""
  for i in range (len(decode)):
    decoded_message = decoded_message + chr(ord(decode[i]) + 3)
  print (encoded_message)