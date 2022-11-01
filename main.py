import random
import string

chars=int(input("password chars: "))

def letters(x):

    lets=string.ascii_letters
    letterList=[]
    letterStr=""

    for i in lets:
        letterList.append(i)

    i=0

    while i<x:
        letterStr=letterStr + random.choice(letterList)

        i=i+1

    return letterStr



def nums(y):

    n=string.digits
    numList=[]
    numStr=""

    for i in n:
        numList.append(i)
   
    
    i=0

    while i<y:
        numStr=numStr + random.choice(numList)
        i=i+1
    
    return numStr


def symbols(z):
    
    symbs=string.punctuation
    symbList=[]
    symbStr=""

    for i in symbs:
        symbList.append(i)

    i=0

    while i<z:
        symbStr=symbStr + random.choice(symbList)
        i=i+1


    return symbStr



proportionLetters = random.randrange(1,chars-3) #3 is a parameter to make impossible to gen a password with no numbers and symbols

print(proportionLetters)

proportionNums = random.randrange(1,chars-proportionLetters-3) #3 is a parameter to make impossible to gen a password with no symbols

print(proportionNums)

proportionSymbols = chars-(proportionNums+proportionLetters)

print(proportionSymbols)

letterStr=letters(proportionLetters)
numStr=nums(proportionNums) 
symbStr=symbols(proportionSymbols)

pw = letterStr + numStr + symbStr


pwList=[]

for i in pw:
    pwList.append(i)

random.shuffle(pwList)
password=""

for i in pwList:
    password=password+i

print(password)



