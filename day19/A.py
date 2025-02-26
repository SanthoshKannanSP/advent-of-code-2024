with open("input.txt","r") as f:
    data = [line.strip() for line in f.readlines()]

blocks = data[0].split(",")
blocks = [block.strip() for block in blocks]

def isWordPossible(word,startIndex):
    if startIndex>=len(word):
        return True
    for block in blocks:
        if word[startIndex:].startswith(block):
            M = len(block)
            if isWordPossible(word,startIndex+M):
                return True
    return False

ans = 0
for word in data[2:]:
    N = len(word)
    if isWordPossible(word,0):
        ans+=1

print(ans)