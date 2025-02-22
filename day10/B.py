with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

M,N = len(data),len(data[0])
directions = [(0,1),(0,-1),(1,0),(-1,0)]
peaks_dict = dict()

def dfs(prev,row,col):
    if row<0 or row>=M or col<0 or col>=N:
        return 0
    height = int(data[row][col])
    if height!=prev+1:
        return 0
    if height==9:
        return 1
    if (row,col) in peaks_dict:
        return peaks_dict[(row,col)]
    
    peaks = 0
    for dr,dc in directions:
        peaks += dfs(height,row+dr,col+dc)

    peaks_dict[(row,col)] = peaks
    return peaks
    
ans = 0
for row in range(M):
    for col in range(N):
        if data[row][col]=="0":
            ans += dfs(-1,row,col)

print(ans)