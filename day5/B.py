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


incorrect_update = []

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

        
    if flag:
        incorrect_update.append(update)

ans = 0
for update in incorrect_update:
    correct_update = []
    visited = set()

    for page in update:
        temp = []
        for depend in dependency[page]:
            while depend in visited:
                prev = correct_update.pop()
                temp.append(prev)
                visited.remove(prev)
                
        correct_update.append(page)
        visited.add(page)
        while temp:
            val = temp.pop()
            correct_update.append(val)
            visited.add(val)

    N = len(correct_update)
    ans += correct_update[N//2]
            
print(ans)