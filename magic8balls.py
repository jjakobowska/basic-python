#two ways of a magic 8 ball
import random

#with elif 
def FirstMagicBall():
    def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'certain'
        elif answerNumber == 2:
            return 'decidedly so'
        elif answerNumber == 3:
            return 'yes'
        elif answerNumber == 4:
            return 'try agin :/'
        elif answerNumber == 5:
            return 'later'
        elif answerNumber == 6:
            return 'ask again'
        elif answerNumber == 7:
            return 'no'
        elif answerNumber == 8:
            return 'very doubtful'
    # or print(getAnswer(random.randint(1,8)))
    r = random.randint(1,8)
    fortune = getAnswer(r)
    print(fortune)
#now with a list
def SecondMagicBall():
    messages = ['certain', 'decidedly so','yes', 'try agin :/' ,'later' ,'ask again' ,'no','very doubtful']
    print(messages[random.randint(0,len(messages)-1)])
FirstMagicBall()
SecondMagicBall()
