from collections import defaultdict

rules = []

with open("input.txt","r") as f:
    while line:=f.readline().strip():
        rules.append(line)

    updates = f.readlines()

rules = [list(map(int,line.strip().split("|"))) for line in rules]
updates = [list(map(int,line.strip().split(","))) for line in updates]

dependency = defaultdict(list)

for depend,page in rules:
    dependency[depend].append(page)


ans=0

for update in updates:
    flag = False
    visited = set()
    for page in update:
        for depend in dependency[page]:
            if depend in visited:
                flag = True
                break
        if flag:
            break
        visited.add(page)

        
    if not flag:
        N = len(update)
        ans+=update[N//2]

print(ans)