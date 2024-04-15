#https://codeforces.com/contest/1216/problem/C

def area(t):
    return(t[2]-t[0])*(t[3]-t[1])
def overlap(t1, t2):
    x1, y1, x2, y2=t1
    x3, y3, x4, y4=t2
    if x1>=x4 or x2<=x3 or y1>=y4 or y2<=y3:
        return(0, 0, 0, 0)
    else:
        return max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4)
t1=tuple(map(int, input().split()))
t2=tuple(map(int, input().split()))
t3=tuple(map(int, input().split()))

ta=area(t1)-area(overlap(t1, t2))-area(overlap(t1, t3))+area(overlap(overlap(t1, t2),t3))

if ta==0:
    print("NO")
else:
    print("YES")