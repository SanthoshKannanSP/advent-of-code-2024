with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip() for line in data]
M = len(data)
N = len(data[0])

def isValid(row,col):
    if row-1<0 or row+1>=M or col-1<0 or col+1>=N:
        return False
    
    tlbr = data[row-1][col-1]+data[row+1][col+1]
    trbl = data[row-1][col+1]+data[row+1][col-1]

    if (tlbr=="SM" or tlbr=="MS") and (trbl=="SM" or trbl=="MS"):
        return True

    return False

ans = 0
for row in range(M):
    for col in range(N):
        if data[row][col]=="A":
            if isValid(row,col):
                ans+=1
print(ans)