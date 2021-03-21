#importing modules
#random and sys

import random
import sys
       
def randommm():
    for i in range(5):
        print(random.randint(1,10))

def sysExit():
    while True:
        print('Type exit to exit')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed ' + response )
randommm()
sysExit()
