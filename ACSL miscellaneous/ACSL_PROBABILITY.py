data = "2, 10, 8, N, B, B"
data = data.split(", ")

R=int(data[1])
B=int(data[2])
i=data[3]
r=data[3]


def case1(R, B, i):
    q=R+B
    q=str(q)
    R=str(R)
    B=str(B)
    if i=="R":
        return R+"/"+q
    else:
        return B+"/"+q

def case2(R, B, o1, o2):
    if (o1=="R" and o2=="B") or (o1=="B" and o2=="R"):
        q=R+B
        qq=q*q
        w=R*B
        qq=str(qq)
        w=str(w)
        return w+"/"+qq
    elif o1=="R" and o2=="R":
        q=R+B
        qq=q*q
        w=R*R
        qq=str(qq)
        w=str(w)
        return w+"/"+qq
    elif o1=="B" and o2=="B":
        q=R+B
        qq=q*q
        w=B+B
        qq=str(qq)
        w=str(w)
        return w+"/"+qq

def case3(R, B, o1, o2):
    if (o1=="R" and o2=="B") or (o1=="B" and o2=="R"):
        q=R+B
        qq=q*(q-1)
        w=R*B
        qq=str(qq)
        w=str(w)
        return w+"/"+qq
    elif o1=="R" and o2=="R":
        q=R+B
        qq=q*(q-1)
        w=R*R
        qq=str(qq)
        w=str(w)
        return w+"/"+qq
    elif o1=="B" and o2=="B":
        q=R+B
        qq=q*(q-1)
        w=B*(B-1)
        qq=str(qq)
        w=str(w)
        return w+"/"+qq
    
    
if data[0]=="1":
    print(case1(R, B, i))
else:
    o1=data[4]
    o2=data[5]
    if r=="Y":
        print(case2(R, B, o1, o2))
    else:
        print(case3(R, B, o1, o2))
    
