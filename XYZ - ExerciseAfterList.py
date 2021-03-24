#user gives a list and it comes out as a strings made of values from list separated by comas
def separated():
    spam = []
    while True:
        print('give me things to add to list or just press enter to end adding')
        things = input()
        if things == '':
            break
        spam = spam + [things]
    joinedstring = ', '.join(spam)
    print(joinedstring )

spam = []
separated()
