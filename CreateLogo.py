'''
Multiple times we have seen a logo, that itself is a word but stands acronym for multiple connected words.
The project aims to get all such words when user specifies the listOfWords.

Current script limits the words to 3 per execution.

'''

__author__ = 'tusharsaurabh'

import enchant

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
listOfWords = ["Innovate", "Experiment","Speak"]

sizeOfList = len(listOfWords)
x = 0
for y in range(0, sizeOfList):
    maxwordloop1 = getmaximumlength(listOfWords[x])
    maxwordloop2 = getmaximumlength(listOfWords[x+1])
    maxwordloop3 = getmaximumlength(listOfWords[x+2])
    for i in range(1, maxwordloop1 + 1):
        firstPart = listOfWords[x][0:i]
        for j in range(1, maxwordloop2 + 1):
            secondPart = listOfWords[x + 1][0:j]
            for k in range(1, maxwordloop3 + 1):
                thirdPart = listOfWords[x + 2][0:k]
                if dictionary.check((firstPart + secondPart + thirdPart).lower()):
                    print "Logo is %s,Tagling is %s, %s, %s" % (
                        (firstPart + secondPart + thirdPart).lower(), firstPart.lower(), secondPart.lower(), thirdPart.lower())
    rearrangelist(listOfWords)
