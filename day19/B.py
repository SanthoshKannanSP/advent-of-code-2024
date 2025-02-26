from functools import lru_cache

with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

blocks = data[0].split(",")
blocks = [block.strip() for block in blocks]

@lru_cache(None)
def isWordPossible(word,startIndex):
    if startIndex>=len(word):
        return 1
    ways = 0
    for block in blocks:
        if word[startIndex:].startswith(block):
            M = len(block)
            ways += isWordPossible(word,startIndex+M)
    return ways

ans = 0
for word in data[2:]:
    ans += isWordPossible(word,0)

print(ans)