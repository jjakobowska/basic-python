def whileloop():
  name = ' '
  while name != 'your name':
      print('Type your name')
      name = input()
  print('Thank you')
  
def breakstatement():
    while True:
        print('Type your name')
        name = input()
        if name == 'your name':
            break
    print('Thank you')


whileloop()
breakstatement()
