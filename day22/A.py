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
for number in numbers:
    nextSecret = number
    for level in range(2000):
        nextSecret = process1(nextSecret)
        nextSecret = process2(nextSecret)
        nextSecret = process3(nextSecret)
    ans += nextSecret

print(ans)