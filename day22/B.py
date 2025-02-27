from collections import defaultdict, deque
with open("input.txt","r") as f:
    numbers = list(map(int,f.readlines()))

def process1(num):
    result = num*64
    mixed = num ^ result
    pruned = mixed % 16777216
    return pruned

def process2(num):
    result = num//32
    mixed = num ^ result
    pruned = mixed % 16777216
    return pruned

def process3(num):
    result = num * 2048
    mixed = num ^ result
    pruned = mixed % 16777216
    return pruned

ans = 0
totalPrice = defaultdict(int)
for number in numbers:
    nextSecret = number
    currentWindow = deque([(number%10,None)])
    viewedSequences = set()

    for level in range(2000):
        nextSecret = process1(nextSecret)
        nextSecret = process2(nextSecret)
        nextSecret = process3(nextSecret)
        currentPrice = nextSecret%10
        changePrice = currentPrice - currentWindow[-1][0]
        currentWindow.append((currentPrice,changePrice))
        if level>=2:
            sequence = tuple([value[1] for value in currentWindow])
            if sequence not in viewedSequences:
                viewedSequences.add(sequence)
                totalPrice[sequence] += currentPrice
            currentWindow.popleft()

print(max(totalPrice.values()))