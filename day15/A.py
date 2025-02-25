with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

index = 0
L = len(data)

grid = []
while index<L and data[index]:
    grid.append([char for char in data[index]])
    index += 1

index += 1
moves = ""

while index<L:
    moves += data[index]
    index += 1

R,C = len(grid),len(grid[0])
M = len(moves)

posX,posY = 0,0

for row in range(R):
    for col in range(C):
        if grid[row][col]=="@":
            posX,posY = row,col
            break

directionMap = {
    "^":(-1,0),
    ">":(0,1),
    "v":(1,0),
    "<":(0,-1)
}

def updatePos(posX,posY,dx,dy):
    newX = posX+dx
    newY = posY+dy
    while grid[newX][newY]!="." and grid[newX][newY]!="#":
        newX += dx
        newY += dy

    if grid[newX][newY]==".":
        while grid[newX-dx][newY-dy]!="@":
            grid[newX][newY]=grid[newX-dx][newY-dy]
            newX-=dx
            newY-=dy
        grid[newX][newY]=grid[newX-dx][newY-dy]
        grid[newX-dx][newY-dy]="."
        return newX,newY
    else:
        return posX,posY

for move in moves:
    dx,dy = directionMap[move]
    posX,posY = updatePos(posX,posY,dx,dy)

def findDistance(row,col):
    return row*100 + col

ans = 0
for row in range(R):
    for col in range(C):
        if grid[row][col]=="O":
            ans += findDistance(row,col)

print(ans)