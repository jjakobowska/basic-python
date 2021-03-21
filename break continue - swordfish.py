# ask for a name and password
#continue


while True:
    print('Who are you')
    name = input()
    if name != 'Joe':
          continue
    print('Hello, what is a password?(it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
        
