with open("input.txt","r") as f:
    data = f.readlines()

data = [list(map(int,line.strip().split())) for line in data]

def isMonotonic(diff,levels):
    for index in range(levels-1):
        if diff[index]*diff[index+1]<=0 or (abs(diff[index])>3 or abs(diff[index+1])>3):
            return False
    return True

ans = 0
for report in data:
    levels = len(report)
    diff = [report[idx]-report[idx+1] for idx in range(levels-1)]
    
    if isMonotonic(diff,levels-1):
        ans+=1
        continue

    for idx in range(levels):
        new_report = [report[i] for i in range(levels) if i!=idx]
        diff = [new_report[i]-new_report[i+1] for i in range(levels-2)]
        
        if isMonotonic(diff,levels-2):
            ans += 1
            break
        
print(ans)