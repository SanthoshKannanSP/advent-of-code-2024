import heapq
with open("input.txt","r") as f:
    grid = [line.strip() for line in f.readlines()]

R,C = len(grid),len(grid[0])
startX,startY = -1,-1
endX,endY = -1,-1

for row in range(R):
    for col in range(C):
        if grid[row][col]=="S":
            startX,startY = row,col
        if grid[row][col]=="E":
            endX,endY = row,col

seenCost = dict()
stack = [(startX,startY,0,1,0)]
minCost = float("inf")

while stack:
    row,col,dr,dc,cost = stack.pop()
    if row==endX and col==endY:
        minCost = min(minCost,cost)
        continue
    if grid[row][col]=="#":
        continue
    if (row,col,dr,dc) in seenCost:
        if seenCost[(row,col,dr,dc)]<cost:
            continue
    if cost>minCost:
        continue
    seenCost[(row,col,dr,dc)] = cost
    stack.append((row,col,dc,dr,cost+1000))
    stack.append((row,col,dc*-1,dr*-1,cost+1000))
    stack.append((row+dr,col+dc,dr,dc,cost+1))

minCost = min(seenCost.get((endX,endY,-1,0),minCost),seenCost.get((endX,endY,0,1),minCost))
directions = ((-1,0),(1,0),(0,1),(0,-1))
stack = [(endX,endY,-1,0,minCost),(endX,endY,0,1,minCost)]
goodSeats = set()
while stack:
    row,col,dr,dc,cost = stack.pop()
    if grid[row][col]=="#":
        continue
    goodSeats.add((row,col))
    for nr,nc in directions:
        if nr==dr and nc==dc and seenCost.get((row-dr,col-dc,dr,dc),float("inf"))==cost-1:
            stack.append((row-dr,col-dc,dr,dc,cost-1))
        elif seenCost.get((row-nr,col-nc,nr,nc),float("inf"))==cost-1001:
            stack.append((row-nr,col-nc,nr,nc,cost-1001))

print(len(goodSeats))