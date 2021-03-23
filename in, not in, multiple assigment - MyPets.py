# sprawdza czy to zwierze jest moje czy nie
myPets = ['Zo' , 'Poka' , 'It']
print('enter a pet name:')
name = input()
if name in myPets:
    print(name + ' is my pet')
elif name not in myPets:
    print( name + ' is not my pet')

#jest sobie kot i robimy multiple assigment
cat = ['fat' , 'black' , 'loud' ]
size, colour, disposition = cat
print(cat)
print('My cat is ' + size + ' ' + colour + ' '+ disposition)

