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
    count = 0
    for x in range(posX-20,posX+21):
        for y in range(posY-20+abs(posX-x),posY+21-abs(posX-x)):
            if 0<=x<M and 0<=y<N and (x,y) in dp:
                currTime = dp[(x,y)]+abs(posX-x)+abs(posY-y)+(minTime-dp[(posX,posY)])
                if minTime-currTime>=100:
                    count+=1
    return count
                    
for posX,posY in dp.keys():
    ans += findCheatCount(posX,posY,minTime,dp,M,N)
print(ans)