with open("input.txt","r") as f:
    data = f.readline()

disk = []

for idx,count in enumerate(data):
    if idx%2==0:
        for i in range(int(count)):
            disk.append(idx//2)
    else:
        for i in range(int(count)):
            disk.append(-1)

left = 0
right = len(disk)-1

while left<right:
    if disk[left]!=-1:
        left+=1
    elif disk[right]==-1:
        right-=1
    else:
        disk[left],disk[right] = disk[right],disk[left]
        left+=1
        right-=1

ans = 0
for idx,id in enumerate(disk):
    if id==-1:
        continue
    ans += idx*id

print(ans)