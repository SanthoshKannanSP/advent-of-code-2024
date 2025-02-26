with open("input.txt","r") as f:
    walls = set(tuple(map(int,line.split(","))) for line in f.readlines()[:1024])

stack = [(0,0,0)]
seen = dict()
directions = [(0,1),(0,-1),(1,0),(-1,0)]

while stack:
    row,col,step = stack.pop()
    if row<0 or row>70 or col<0 or col>70:
        continue
    if (row,col) in walls:
        continue
    if (row,col) in seen and seen[(row,col)]<=step:
        continue
    seen[(row,col)] = step
    if row==70 and col==70:
        continue
    for dr,dc in directions:
        stack.append((row+dr,col+dc,step+1))

print(seen[(70,70)])