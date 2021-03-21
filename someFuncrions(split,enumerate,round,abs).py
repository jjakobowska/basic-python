# splits a string into a list
def spliting():
    print('split function:')
    txt = "Welcome to the jungle"
    x = txt.split()
    print(x)
#take a collection and returns it as an enumerate object
def enumerating():
    print('enumerate function:')
    x = ('apple','banana','orange')
    y = enumerate(x)
    print(list(y))       
# zaokrąglanie (liczba, liczba miejsc po przecinku po zaokrągleniu)
def rounding():
    print('round function:')
    x = round(5.76543, 2)
    print(x)
# wartośc bezwzględna
def absing():
    print('abs function:')
    x = abs(-7.25)
    y = 3 - 4j
    z = -2
    print(x, abs(y), abs(z))
          
spliting()            
enumerating()
rounding()
absing()
