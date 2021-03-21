#five times jimmy
#for loop

def loop():
    print('(l)My name is')
    for i in range(5):
        print('Jimmy five times('+str(i)+')')

def EquivalentWhileLoop():
    print('(wl)My name is')
    i = 0
    while i < 5:
        print('Jimmy five times('+str(i)+')')
        i = i + 1
loop()
EquivalentWhileLoop()
