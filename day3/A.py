import re

with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

pattern = r"mul\(\d{1,3}\,\d{1,3}\)"

ans = 0

for line in data:
    matches = re.findall(pattern,line)
    numbers = [tuple(map(int,match.lstrip(r"mul(").rstrip(r")").split(","))) for match in matches]

    for x,y in numbers:
        ans += x*y

print(ans)