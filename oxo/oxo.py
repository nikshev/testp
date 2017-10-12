import json

wins = [
    "111000000", "000111000", "000000111",    # Across
    "100100100", "010010010", "001001001",    # Down
    "100010001", "001010100"                  # Diagonal
]


#Create string from array for X
def createStringX(row):
    row_str = []
    for value in row:
        index = (value[0]*3)+value[1]
        if value[2] == 'X':
            row_str.insert(index, "1")
        else:
            row_str.insert(index, "0")
    for i in range(9-len(row_str)):
        row_str.insert(index, "0")
    return ''.join(row_str)

#Create string from array for O
def createStringO(row):
    row_str = []
    for value in row:
        index = (value[0]*3)+value[1]
        if value[2] == 'O':
            row_str.insert(index, "1")
        else:
            row_str.insert(index, "0")
    for i in range(9-len(row_str)):
        row_str.insert(index, "0")
    return ''.join(row_str)


#Compare win string and current string
def isDraw(row_str_X, row_str_O):
    for wins_str in wins:
        if (wins_str == row_str_X):
            return False
        if (wins_str == row_str_O):
            return False
    return True


#Check draws
def checkDraw(row):
    return isDraw(createStringX(row), createStringO(row))

#Main function
draws=0;
with open('oxosatae.json') as json_data:
    data = json.load(json_data)
    for row in data:
        if checkDraw(row):
            draws+=1
print(draws)