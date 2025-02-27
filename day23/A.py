from collections import defaultdict
from itertools import product

with open("input.txt","r") as f:
    links = [line.strip().split("-") for line in f.readlines()]

graph = defaultdict(set)
for u,v in links:
    graph[u].add(v)
    graph[v].add(u)

ans = 0
mainVisited = set()
for u in graph.keys():
    if u[0]!="t":
        continue
    visited = set()
    mainVisited.add(u)
    for v,w in list(product(graph[u],repeat=2)):
        if v==w:
            continue
        if (w,v) in visited or w in mainVisited or v in mainVisited:
            continue
        visited.add((v,w))
        if w in graph[v] and v in graph[w]:
            ans += 1
    
print(ans)