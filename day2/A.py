with open("input.txt","r") as f:
    data = f.readlines()

data = [list(map(int,line.strip().split())) for line in data]

ans = 0
for report in data:
    increasing = report[1]-report[0]>0
    levels = len(report)
    flag = False
    if increasing:
        for idx in range(1,levels):
            diff = report[idx]-report[idx-1]
            if diff<=0 or diff>3:
                flag = True
                break
    else:
        for idx in range(1,levels):
            diff = report[idx-1]-report[idx]
            if diff<=0 or diff>3:
                flag=True
                break
    
    if not flag:
        ans+=1

print(ans)