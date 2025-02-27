with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]


directions = ((0,1),(0,-1),(1,0),(-1,0))
M,N = len(data),len(data[0])
startX,startY = 0,0
endX,endY = 0,0

for row in range(M):
    for col in range(N):
        if data[row][col]=="S":
            startX,startY = row,col
        if data[row][col]=="E":
            endX,endY = row,col

dp = dict()
def findMinTime(posX,posY,prevX,prevY):
    time = 0
    while data[posX][posY]!="S":
        dp[(posX,posY)]=time
        for dx,dy in directions:
            if data[posX+dx][posY+dy]!="#" and (posX+dx!=prevX or posY+dy!=prevY):
                prevX = posX
                prevY = posY
                posX += dx
                posY += dy
                time+=1
                break
    dp[(posX,posY)] = time
    return time
      
ans = 0
minTime = findMinTime(endX,endY,-1,-1)

def findCheatCount(posX,posY,minTime,dp,M,N):
    savedTimes = 0
    for dx,dy in directions:
        if data[posX+dx][posY+dy]=="#":
            for dr,dc in directions:
                if 0<=posX+dx+dr<M and 0<=posY+dy+dc<N and data[posX+dx+dr][posY+dy+dc] in (".","E") and (dr*-1!=dx or dc*-1!=dy):
                    currTime = dp[(posX+dx+dr,posY+dy+dc)] + (minTime-dp[(posX,posY)]) + 2
                    if minTime-currTime<100:
                        continue
                    savedTimes += 1
    return savedTimes
                    

for startX,startY in dp.keys():
    ans += findCheatCount(startX,startY,minTime,dp,M,N)
print(ans)