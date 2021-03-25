#jest dictionary z osobami i ich urodzinami 
#jeżeli dana osoba jest w dictionary to jest podawana jej data urodzenia
#jeżeli nie to program pyta o date urodzenia  i dodaje osobe z datą do zbioru
birthdays = {'Wika' : 'Apr 20' , 'Waleria' : 'Apr 28' , 'Piotrek' : 'July 21'}

while True:
    print('Enter a name or '' to quit')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print(' I dont have birthday information for ' + name)
        print(' when is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
