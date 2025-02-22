with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

M,N = len(data),len(data[0])
directions = [(0,1),(0,-1),(1,0),(-1,0)]
peaks_dict = dict()

def search(startRow,startCol):
    peaks = 0
    stack = [(-1,startRow,startCol)]
    visited = set()

    while stack:
        prev,row,col = stack.pop()
        if row<0 or row>=M or col<0 or col>=N:
            continue
        if (row,col) in visited:
            continue
        height = int(data[row][col])
        if height!=prev+1:
            continue
        if height==9:
            peaks+=1
        else:
            for dr,dc in directions:
                stack.append((height,row+dr,col+dc))
        visited.add((row,col))
    
    return peaks
    
ans = 0
for row in range(M):
    for col in range(N):
        if data[row][col]=="0":
            ans += search(row,col)

print(ans)