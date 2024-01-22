from random import choice
# function to check if all items in an array match
# input an array to check
def is_same(row):
    temp = True
    symbol = row[0]
    for i in row:
        if i != symbol:
            temp = False
    return(temp)

# generate a random 3 by 3 field of either "X" or "O"
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
    if is_same(row) == True:
        trinity = True
        break

# check for match in columns if there is none in rows
if trinity == False:
    new_field = [[0,0,0],[0,0,0],[0,0,0]]
    collumn_coord = 0
    while collumn_coord < 3:
        row_coord = 0
        while row_coord < 3:
            newField[collumn_coord][row_coord] = field[row_coord][collumn_coord]
            row_coord += 1
        collumn_coord += 1
    
    for collumn in newField:
        if is_same(collumn) == True:
            trinity = True
            break

# check for match in diagonal (only checks if 3 symbols match)
if trinity == False:
    diagonals = [[field[0][0], field[1][1], field[2][2] ],
                 [field[0][2] , field[1][1], field[2][0]]]
    for diag in diagonals:
        if is_same(diag) == True:
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
