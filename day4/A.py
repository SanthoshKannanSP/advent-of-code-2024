with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

pattern = "XMAS"

M = len(data)
N = len(data[0])

def search(row,col):
    directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,1),(1,-1)]

    ans = 0
    for dx,dy in directions:
        sx,sy = row,col
        index = 0
        while index<4:
            if sx<0 or sx>=M or sy<0 or sy>=N:
                break

            if data[sx][sy]!=pattern[index]:
                break
            sx+=dx
            sy+=dy
            index+=1
            
        else:
            ans += 1
        
    return ans


ans = 0
for row in range(M):
    for col in range(N):
        if data[row][col]==pattern[0]:
            matches = search(row,col)
            ans+=matches

print(ans)