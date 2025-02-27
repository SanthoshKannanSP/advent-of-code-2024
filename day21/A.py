with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

numPad = {'7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), '0': (1, 3), 'A': (2, 3)}
dirPad = {'^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}
movementMap = dict()

for num1 in numPad.keys():
    x1,y1 = numPad[num1]
    for num2 in numPad.keys():
        x2,y2 = numPad[num2]
        numPair = (num1, num2)
        if x1 == x2:
            movementMap[numPair] = ('v' if y1 < y2 else '^') * abs(y1 - y2)
        elif y1 == y2:
            movementMap[numPair] = ('>' if x1 < x2 else '<') * abs(x1 - x2)
        else:
            if x1 == 0 and y2 == 3:
                movementMap[numPair] = '>' * (x2 - x1) + 'v' * (y2 - y1)
            elif y1 == 3 and x2 == 0:
                movementMap[numPair] = '^' * (y1 - y2) + '<' * (x1 - x2)
            else:
                movementMap[numPair] = [('v' if y1 < y2 else '^') * abs(y1 - y2), ('>' if x1 < x2 else '<') * abs(x1 - x2)]

for dir1 in dirPad.keys():
    x1,y1 = dirPad[dir1]
    for dir2 in dirPad.keys():
        x2,y2 = dirPad[dir2]
        dir_pair = (dir1, dir2)
        if x1 == x2: movementMap[dir_pair] = ('v' if y1 < y2 else '^') * abs(y1 - y2)
        elif y1 == y2: movementMap[dir_pair] = ('>' if x1 < x2 else '<') * abs(x1 - x2)
        else:
            if x1 == 0 and y2 == 0: movementMap[dir_pair] = '>' * (x2 - x1) + '^'
            elif y1 == 0 and x2 == 0: movementMap[dir_pair] = 'v' + (x1 - x2) * '<'
            else: movementMap[dir_pair] = [('v' if y1 < y2 else '^') * abs(y1 - y2), ('>' if x1 < x2 else '<') * abs(x1 - x2)]

def keypress(i, new_sequence):
    if i == len(sequence):
        sequences.append(new_sequence)
    else:
        presses = movementMap[('A' if i == 0 else sequence[i - 1], sequence[i])]
        if isinstance(presses, list):
            keypress(i + 1, new_sequence + presses[0] + presses[1] + 'A')
            keypress(i + 1, new_sequence + presses[1] + presses[0] + 'A')
        else:
            keypress(i + 1, new_sequence + presses + 'A')

total = 0
for robot1 in data:
    sequences, sequence = [], robot1
    keypress(0, '')
    old_sequences, sequences = sequences, []
    for robot2 in old_sequences:
        sequence = robot2
        keypress(0, '')
    old_sequences, sequences = sequences, []
    for robot3 in old_sequences:
        sequence = robot3
        keypress(0, '')
    total += min([len(sequence) for sequence in sequences]) * int(robot1[:-1])
print(total)