def spam(Db):
    try:
        return 42/Db
    except ZeroDivisionError :
        print('Error: Invalid argument')

def spamm(Db):
    return 42/Db
try:
    print(spamm(2))
    print(spamm(0))
    print(spamm(3)) # nie wykona się bo wcześniej występuje ZeroDivisionError
except ZeroDivisionError :
    print('Error: Invalid argument')



    
print(spam(2))
print(spam(0))
