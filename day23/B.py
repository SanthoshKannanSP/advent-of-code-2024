from collections import defaultdict

with open("input.txt","r") as f:
    links = [line.strip().split("-") for line in f.readlines()]

graph = defaultdict(set)
for u,v in links:
    graph[u].add(v)
    graph[v].add(u)

def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    pivot = next(iter(P.union(X)))
    for v in P - set(graph[pivot]):
        bron_kerbosch(R.union([v]),P.intersection(graph[v]),X.intersection(graph[v]),graph, cliques)
        P.remove(v)
        X.add(v)

cliques = []
bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
max_clique = max(cliques, key=len)
print(",".join(sorted(list(max_clique))))