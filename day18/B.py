with open("input.txt","r") as f:
    data = [tuple(map(int,line.split(","))) for line in f.readlines()]


walls = set()
directions = [(0,1),(0,-1),(1,0),(-1,0)]

index = 0
while index<1024:
    walls.add(data[index])
    index+=1

def doesPathExist(walls):
    stack = [(0,0)]
    seen = set()
    while stack:
        row,col = stack.pop()
        if row==70 and col==70:
            return True
        if row<0 or row>70 or col<0 or col>70:
            continue
        if (row,col) in walls:
            continue
        if (row,col) in seen:
            continue
        seen.add((row,col))
        for dr,dc in directions:
            stack.append((row+dr,col+dc))
    return False

while doesPathExist(walls):
    walls.add(data[index])
    index+=1

print(f"{data[index-1][0]},{data[index-1][1]}")