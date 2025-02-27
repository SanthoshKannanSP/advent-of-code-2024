with open("input.txt","r") as f:
    data = f.read().split("\n\n")

keys = []
locks = []

for entity in data:
    entity = entity.split("\n")
    if entity[0]=="#####":
        locks.append(entity)
    else:
        keys.append(entity)

lockHeights = [[line.count("#") for line in zip(*lock)] for lock in locks]
keyHeights = [[line.count(".") for line in zip(*key)] for key in keys]

ans = 0
for key in keyHeights:
    for lock in lockHeights:
        for i in range(5):
            if lock[i]>key[i]:
                break
        else:
            ans += 1

print(ans)
