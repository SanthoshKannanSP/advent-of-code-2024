import re

with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

pattern = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)"
ans = 0

execute = True
for line in data:
    matches = re.findall(pattern,line)

    for match in matches:
        if match == "do()":
            execute = True
        elif match == "don't()":
            execute = False
        elif execute:
            x,y = list(map(int,match.lstrip(r"mul(").rstrip(")").split(",")))
            ans += x*y

print(ans)