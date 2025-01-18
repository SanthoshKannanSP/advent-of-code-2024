with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

def find_initial_guard_pos(M,N):
    for row in range(M):
        for col in range(N):
            if data[row][col]=="^":
                return row,col
            
M = len(data)
N = len(data[0])

posX, posY = find_initial_guard_pos(M,N)

next_direction = {
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0,-1),
    (0,-1):(-1,0)
}

dx,dy = (-1,0)
ans = 0
visited = set()

while 0<=posX<M and 0<=posY<N:
    if data[posX][posY]=="." and (posX,posY) not in visited:
        ans += 1
        visited.add((posX,posY))
    elif data[posX][posY]=="#":
        posX -= dx
        posY -= dy
        dx,dy = next_direction[(dx,dy)]
    
    posX += dx
    posY += dy

print(ans+1)