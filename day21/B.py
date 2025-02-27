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

known_sequences = {}
def next_robot(new_sequence, level):
    if (new_sequence, level) in known_sequences:
        return known_sequences[(new_sequence, level)]
    if level == 26:
        n = len(new_sequence)
    else:
        n = 0
        for i, c in enumerate(new_sequence):
            presses = movementMap[('A' if i == 0 else new_sequence[i - 1], c)]
            n += min(next_robot(presses[0] + presses[1] + 'A', level + 1), next_robot(presses[1] + presses[0] + 'A', level + 1)) if isinstance(presses, list) else next_robot(presses + 'A', level + 1)
    known_sequences[(new_sequence, level)] = n
    return n

print(sum([next_robot(line, 0) * int(line[:-1]) for line in data]))