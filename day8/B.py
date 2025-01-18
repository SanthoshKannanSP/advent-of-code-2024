from collections import defaultdict

with open("input.txt","r") as f:
    data = f.readlines()

data = [line.strip() for line in data]

antinodes = set()
antenna_locations = defaultdict(list)

M = len(data)
N = len(data[0])

for row in range(M):
    for col in range(N):
        val = data[row][col]
        if val!=".":
            antenna_locations[val].append((row,col))

for locations in antenna_locations.values():
    A = len(locations)
    if A==1:
        continue
    
    for i in range(A):
        first_antenna = locations[i]
        antinodes.add(first_antenna)
        for j in range(A):
            if i==j:
                continue

            second_antenna = locations[j]
            dx = second_antenna[0]-first_antenna[0]
            dy = second_antenna[1]-first_antenna[1]

            antinodeX,antinodeY = second_antenna[0]+dx,second_antenna[1]+dy
            while 0<=antinodeX<M and 0<=antinodeY<N:
                antinodes.add((antinodeX,antinodeY))
                antinodeX+=dx
                antinodeY+=dy

print(len(antinodes))