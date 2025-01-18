with open("input.txt","r") as f:
    data = f.readlines()

data = [list(line.strip()) for line in data]

def find_initial_guard_pos(M,N):
    for row in range(M):
        for col in range(N):
            if data[row][col]=="^":
                return row,col
            
def is_guard_looping(posX,posY):
    dx,dy = (-1,0)
    visited = set()

    while 0<=posX<M and 0<=posY<N:
        if (posX,posY,dx,dy) in visited:
            return True   
        if data[posX][posY]=="#":
            posX -= dx
            posY -= dy
            dx,dy = next_direction[(dx,dy)]
        
        visited.add((posX,posY,dx,dy))
        
        posX += dx
        posY += dy
    
    return False
            
M = len(data)
N = len(data[0])

posX, posY = find_initial_guard_pos(M,N)

next_direction = {
    (-1,0):(0,1),
    (0,1):(1,0),
    (1,0):(0,-1),
    (0,-1):(-1,0)
}

ans = 0

for obsX in range(M):
    for obsY in range(N):
        if data[obsX][obsY]==".":
            data[obsX][obsY] = "#"
            if is_guard_looping(posX,posY):
                ans+=1
            data[obsX][obsY] = "."

print(ans)