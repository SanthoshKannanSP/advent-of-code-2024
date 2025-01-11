with open("input.txt","r") as f:
    data = f.readlines()

data = [list(map(int,line.strip().split())) for line in data]
lst1, lst2 = zip(*data)

lst1 = sorted(lst1)
lst2 = sorted(lst2)

ans = 0
for val1, val2 in zip(lst1,lst2):
    ans += abs(val1-val2)

print(ans)