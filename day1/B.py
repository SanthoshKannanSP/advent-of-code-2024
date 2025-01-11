from collections import Counter

with open("input.txt","r") as f:
    data = f.readlines()

data = [list(map(int,line.strip().split())) for line in data]

lst1,lst2 = zip(*data)
freq = Counter(lst2)

ans = 0
for val in lst1:
    ans += val*freq[val]

print(ans)