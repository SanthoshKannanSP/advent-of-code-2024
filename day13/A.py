with open("/home/santhosh/projects/advent-of-code-2024/day13/input.txt","r") as f:
    data = [line.strip() for line in f.readlines() if line.strip()]

equations = []
current_equation = []

for index,line in enumerate(data):
    if index%3==0:
        x,y = line.lstrip("Button A: X+").split(", Y+")
        current_equation.append(int(x))
        current_equation.append(int(y))
    elif index%3==1:
        x,y = line.lstrip("Button B: X+").split(", Y+")
        current_equation.append(int(x))
        current_equation.append(int(y))
    else:
        x,y = line.lstrip("Prize: X=").split(", Y=")
        current_equation.append(int(x))
        current_equation.append(int(y))
        equations.append(current_equation.copy())
        current_equation.clear()

def solve(u1,u2,v1,v2,y1,y2,c1,c2):
    D = u1*v2 - u2*v1
    Du = y1*v2 - y2*v1
    Dv = u1*y2 - u2*y1

    if D!=0:
        u = Du/D
        v = Dv/D

        if int(u)==u and int(v)==v and u<=100 and v<=100:
            return u*c1 + v*c2
        else:
            return float("inf")
        
    if Du==0 and Dv==0:
        u = y1/u1
        if int(u)==u:
            return u*c1
        
        v = y1/v1
        if int(v)==v:
            return v*c2

    return float("inf")

ans = 0
for u1,u2,v1,v2,y1,y2 in equations:
    cost = solve(u1,u2,v1,v2,y1,y2,3,1)
    if cost!=float("inf"):
        ans += cost

print(int(ans))