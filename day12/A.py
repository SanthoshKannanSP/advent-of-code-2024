with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

M,N = len(data),len(data[0])
directions = ((0,1),(0,-1),(1,0),(-1,0))

ans = 0
visited = set()

for row in range(M):
    for col in range(N):
        if (row,col) in visited:
            continue

        char = data[row][col]
        stack = [(row,col)]
        area = 0
        perimeter = 0

        while stack:
            r,c = stack.pop()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            area += 1

            for dr,dc in directions:
                if 0<=r+dr<M and 0<=c+dc<N:
                    if data[r+dr][c+dc]!=char:
                        perimeter+=1
                    else:
                        stack.append((r+dr,c+dc))
                else:
                    perimeter+=1

        ans += area*perimeter

print(ans)