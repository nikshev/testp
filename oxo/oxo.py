import json

wins = [
    '111 000 000', '000 111 000', '000 000 111',    # Across
    '100 100 100', '010 010 010', '001 001 001',    # Down
    '100 010 001', '001 010 100'                  # Diagonal
]

# Store winning boards as integers
wins = [int(w.replace(' ', ''), 2) for w in wins]

# Returns True if board is a winning position
winning_board = lambda b: any((b & w) == w for w in wins)

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
    if (winning_board(int(row_str_X,2))):
        return False
    if (winning_board(int(row_str_O,2))):
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