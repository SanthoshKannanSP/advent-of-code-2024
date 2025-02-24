import re
from collections import defaultdict

with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

data = [list(map(int,re.findall("-?[0-9]+",line))) for line in data]
M,N = 103,101
count = defaultdict(int)

for y,x,vy,vx in data:
    x += vx*100
    y += vy*100

    if x<0:
        x += M*100
    if y<0:
        y += N*100
    
    x%=M
    y%=N

    count[(x,y)]+=1

ans = 1

def find_count(startRow,endRow,startCol,endCol):
    mul = 0
    for row in range(startRow,endRow):
        for col in range(startCol,endCol):
            if (row,col) in count:
                mul += count[(row,col)]
    return mul

ans*=find_count(0,M//2,0,N//2)
ans*=find_count(M//2 + 1,M,0,N//2)
ans*=find_count(0,M//2,N//2 + 1,N)
ans*=find_count(M//2 + 1,M,N//2 + 1,N)
print(ans)