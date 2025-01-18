with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip().split(":") for line in data]
data = [list(map(int,(line[0],*line[1].split()))) for line in data]

ans = 0

for line in data:
    target = line[0]
    N = len(line)

    stack = [(0,1)]

    while stack:
        current, idx = stack.pop()
        if current>target:
            continue
        if idx==N:
            if current==target:
                ans+=target
                break
            continue
        stack.append((current+line[idx],idx+1))
        stack.append((current*line[idx],idx+1))
        stack.append((int(str(current)+str(line[idx])),idx+1))

print(ans)