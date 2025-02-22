from functools import lru_cache
with open("input.txt","r") as f:
    data = list(map(int,f.readline().strip().split()))
    
@lru_cache(None)
def count(value,d=75):
    if d==0:
        return 1
    if value==0:
        return count(1,d-1)
    
    l = len(str(value))
    if l%2==0:
        value = str(value)
        return count(int(value[:l//2]),d-1) + count(int(value[l//2:]),d-1)
    
    return count(value*2024,d-1)

ans = 0
for value in data:
    ans += count(value)

print(ans)