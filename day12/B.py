with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

M,N = len(data),len(data[0])
directions = ((0,1),(0,-1),(1,0),(-1,0))
cpairs = ((-1,-1),(1,1),(-1,1),(1,-1))

ans = 0
visited = set()

for row in range(M):
    for col in range(N):
        if (row,col) in visited:
            continue

        char = data[row][col]
        stack = [(row,col)]
        region = set()
        while stack:
            r,c = stack.pop()
            if (r,c) in region:
                continue
            region.add((r,c))

            for dr,dc in directions:
                if 0<=r+dr<M and 0<=c+dc<N and data[r+dr][c+dc]==char:
                    stack.append((r+dr,c+dc))

        visited |= region
        corners = 0
        for r,c in region:
            for dr,dc in cpairs:
                if (r+dr,c) in region and (r,c+dc) in region and (r+dr,c+dc) not in region:
                    corners += 1
                if (r+dr,c) not in region and (r,c+dc) not in region:
                    corners += 1
        ans += len(region)*corners

print(ans)