import argparse
import random
import string


def main():

    parser=argparse.ArgumentParser(
            prog='passwordGenerator',
            description='This program randomize a password with numbers, letters and symbols',
            epilog='by BetThical'
            )

    parser.add_argument("characters")
    args=parser.parse_args()


    chars=int(args.characters)

    proportionLetters = random.randrange(1,chars-3) #3 is a parameter to make impossible to gen a password with no numbers and symbols
    proportionNums = random.randrange(1,chars-proportionLetters-3) #3 is a parameter to make impossible to gen a password with no symbols
    proportionSymbols = chars-(proportionNums+proportionLetters)

    
    letterStr=letters(proportionLetters)
    numStr=nums(proportionNums) 
    symbStr=symbols(proportionSymbols)

    string = letterStr + numStr + symbStr


    pwList=[]

    for i in string:
        pwList.append(i)

    random.shuffle(pwList)
    password=""

    for i in pwList:
       password=password+i

    return password


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



print(main())

