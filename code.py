from random import choice
# function to check if 3 symbols match
def isSame(row):
    temp = True
    symbol = row[0]
    for i in row:
        if i != symbol:
            temp = False
    return(temp)

# generate field
options = ("X", "O")
field = [[0,0,0],[0,0,0],[0,0,0]]
i = 0
while i < 3:
    f = 0
    while f < 3:
        field[i][f] = choice(options)
        f += 1
    i += 1

# check for match in rows
trinity = False
for row in field:
    if isSame(row) == True:
        trinity = True
        break

# check for match in columns if there is none in rows
if trinity == False:
    newField = [[0,0,0],[0,0,0],[0,0,0]]
    colCoord = 0
    while colCoord < 3:
        rowCoord = 0
        while rowCoord < 3:
            newField[colCoord][rowCoord] = field[rowCoord][colCoord]
            rowCoord += 1
        colCoord += 1
    
    for column in newField:
        if isSame(column) == True:
            trinity = True
            break

# check for match in diagonal
if trinity == False:
    diagonals = [[field[0][0], field[1][1], field[2][2] ],
                 [field[0][2] , field[1][1], field[2][0]]]
    for diag in diagonals:
        if isSame(diag) == True:
            trinity = True
            break

# print out result
if trinity == True:
    print("Match")
else:
    print("Not match")

# print out the field
print(" ")
print(field[0])
print(field[1])
print(field[2])
