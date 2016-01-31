'''
Multiple times we have seen a logo, that itself is a word but stands acronym for multiple connected words.
The project aims to get all such words when user specifies the listOfWords.

However this project creates all combination and hence would need a supercomputer :D to execute the script.

Please dont run it at home.
'''

import enchant
import itertools

__author__ = 'tusharsaurabh'


def rearrangelist(inputList):
    temp = inputList[0]
    for i in range(1, len(inputList)):
        inputList[i - 1] = inputList[i]

    inputList[len(inputList) - 1] = temp
    return


def getmaximumlength(inputStr):
    MAXWORD = 4

    if len(inputStr) > 4:
        return MAXWORD
    else:
        return len(inputStr)


dictionary = enchant.Dict("en-US")
listOfWords = ["Innovate", "Experiment","Speak","Influence","Lead","Talk","Communicate","Convey","Mistake","Learn","perform"]
sizeOfList = len(listOfWords)
x = 0

#taking 2 at a time
for z in range(1,sizeOfList):
    maxwordloop1 = getmaximumlength(listOfWords[x])
    for i in range(1, maxwordloop1 + 1):
        firstPart = listOfWords[x][0:i]
        loop = True
        j = 1
        while (loop):
            maxwordloop2 = getmaximumlength(listOfWords[x + 1])
            secondPart = listOfWords[x + 1][0:j]
            if dictionary.check((firstPart + secondPart).lower()):
                    print "Logo is %s,Tagling is %s, %s" % (
                        (firstPart + secondPart).lower(), listOfWords[x].lower(), listOfWords[x + 1].lower())
            j += 1
            if j == (maxwordloop2 + 1) or j > len(listOfWords[x + 1]):
                j = 1
                x += 1
                if (x < (sizeOfList - 1)):
                    x = 0
                    loop = False
    rearrangelist(listOfWords)

rearrangelist(listOfWords)
tempList = listOfWords
allpermutations = list(itertools.permutations(tempList))

for listOfWords in allpermutations:
    x = 0
    z = 1
    #taking 3 at a time
    while   True:

        y = 1
        maxwordloop1 = getmaximumlength(listOfWords[x])


        for i in range(1, maxwordloop1 + 1):
            firstPart = listOfWords[x][0:i]
            loop = True
            while (loop):
                maxwordloop2 = getmaximumlength(listOfWords[x+y])
                for j in range(1, maxwordloop2 + 1):
                    secondPart = listOfWords[x + y][0:j]
                    a = 1
                    innerLoop = True
                    while (innerLoop):
                        maxwordloop3 = getmaximumlength(listOfWords[x+y+a])
                        for k in range(1, maxwordloop3 + 1):
                            thirdPart = listOfWords[x + y + 1][0:k]
                            if dictionary.check((firstPart + secondPart + thirdPart).lower()):
                                print "Logo is %s,Tagling is %s, %s, %s" % (
                                (firstPart + secondPart + thirdPart).lower(), listOfWords[x + y + 1].lower(), listOfWords[x + y].lower(), listOfWords[x].lower())
                        a += 1
                        temp1 = a + x + y
                        if temp1 > sizeOfList - 1:
                            a = 1
                            innerLoop = False
                y += 1
                if (x + y > sizeOfList - 2):
                    y = 1
                    loop = False

        rearrangelist(listOfWords)
        z += 1

        if z > sizeOfList - 3:
            break