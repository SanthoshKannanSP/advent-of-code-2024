import re
from statistics import stdev
with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

data = [list(map(int,re.findall("-?[0-9]+",line))) for line in data]
D = len(data)
M,N = 103,101

mx,my = 100,100
ans = 0
for iteration in range(10000):
    x = set()
    y = set()
    for index in range(D):
        data[index][0] += data[index][2]
        data[index][1] += data[index][3]
        data[index][0] %= N
        data[index][1] %= M
        x.add(data[index][0])
        y.add(data[index][1])
    
    if stdev(x)<mx or stdev(y)<my:
        mx = stdev(x)
        my = stdev(y)
        ans = iteration+1

print(ans)
            