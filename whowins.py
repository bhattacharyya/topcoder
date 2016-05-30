#!/usr/bin/python

def whoWins(board):
    countA = 0
    countB = 0
    boundary = 0

    # getInput = list(str(x.strip()) for x in raw_input().split(','))
    getInput = list(str(x.strip()) for x in board.split(','))

    getInput[0] = getInput[0][1:]
    getInput[-1] = getInput[-1][0:-1]

    for k in range(0, len(getInput[0]) - 2):
        getInput[k] = getInput[k][1:-1]

    elements = len(getInput[0])

    iterlimit = (elements / 2) + 1

    for n in range(2, iterlimit + 1):
        numRegions = elements / 2
        boundary += 1

        region1 = []

        for i in range(numRegions - boundary, numRegions + boundary):
            temp1 = list(getInput[i])
            region1.append(temp1[numRegions - boundary:numRegions + boundary])
            region_elements = region1

        for l in region_elements:
            for m in l:
                if m == "A":
                    countA += 1
                if m == "B":
                    countB += 1

        if countA > countB:
            return "Alice"
            break
        if countA < countB:
            return "Bob"
            break
        if countA == countB:
            return "Draw"


vari = raw_input("Enter boardgame : ")
print whoWins(vari)
