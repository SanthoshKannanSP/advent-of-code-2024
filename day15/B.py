from itertools import chain

with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

index = 0
L = len(data)

grid = []
charMap = {
    "#":"##",
    "O":"[]",
    ".":"..",
    "@":"@."
}
while index<L and data[index]:
    grid.append(list(chain.from_iterable((charMap[char][0],charMap[char][1]) for char in data[index])))
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

def pushHorizontal(posX,posY,dy):
    newY = posY+dy
    while grid[posX][newY]!="." and grid[posX][newY]!="#":
        newY += dy

    if grid[posX][newY]==".":
        while grid[posX][newY-dy]!="@":
            grid[posX][newY]=grid[posX][newY-dy]
            newY-=dy
        grid[posX][newY]=grid[posX][newY-dy]
        grid[posX][newY-dy]="."
        return posX,newY
    else:
        return posX,posY
    
def pushVertical(posX,posY,dx):
    if grid[posX+dx][posY]=="#":
        return posX,posY
    if grid[posX+dx][posY]==".":
        grid[posX+dx][posY]="@"
        grid[posX][posY]="."
        return posX+dx,posY
    
    stack = [(posX+dx,posY)]
    if grid[posX+dx][posY]=="]":
        stack.append((posX+dx,posY-1))
    else:
        stack.append((posX+dx,posY+1))
    seen = set()

    while stack:
        x,y = stack.pop()
        if (x,y) in seen:
            continue
        if grid[x][y]=="#":
            return posX,posY
        if grid[x][y]==".":
            continue
        seen.add((x,y))
        stack.append((x+dx,y))
        if grid[x][y]=="]":
            stack.append((x,y-1))
        else:
            stack.append((x,y+1))

    seen = sorted(list(seen),key=lambda x: x[0],reverse= dx==1)
    for x,y in seen:
        grid[x+dx][y] = grid[x][y]
        grid[x][y] = "."

    grid[posX+dx][posY]="@"
    grid[posX][posY]="."
    return posX+dx,posY
        
for move in moves:
    dx,dy = directionMap[move]
    if dx==0:
        posX,posY = pushHorizontal(posX,posY,dy)
    else:
        posX,posY = pushVertical(posX,posY,dx)

def findDistance(row,col):
    return row*100 + col

ans = 0
for row in range(R):
    for col in range(C):
        if grid[row][col]=="[":
            ans += findDistance(row,col)
print(ans)