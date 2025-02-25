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

minCost = float("inf")
seenCost = dict()
stack = [(startX,startY,0,1,0)]

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
    stack.append((row+dr,col+dc,dr,dc,cost+1))
    stack.append((row,col,dc,dr,cost+1000))
    stack.append((row,col,dc*-1,dr*-1,cost+1000))

print(minCost)