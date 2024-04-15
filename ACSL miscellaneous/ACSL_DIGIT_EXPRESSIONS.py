def check2(e):
    count=0
    ops="+-*"
    for op in ops:
        d=eval(e[0]+op+e[1])
        if d>0:
            count+=1
    return count
    
def check3(e):
    count=0
    ops="+-*"
    for op1 in ops:
        ops1=ops.replace(op1,"")
        for op2 in ops1:    
            d=eval(e[0]+op1+e[1]+op2+e[2])
            if d>0:
                count+=1
    return count

def check4(e):
    count=0
    ops="+-*"
    for op1 in ops:
        ops1=ops.replace(op1,"")
        for op2 in ops1:
            ops2=ops1.replace(op2,"")
            for op3 in ops2: 
                d=eval(e[0]+op1+e[1]+op2+e[2]+op3+e[3])
                if d>0:
                    count+=1
    return count

data="02004000600008"
exps=[]
# for x in range(1, len(data)):
#     if data[x]=="0":
#         data.replace(data[x], "")
#     else:
#         break

ndata=""
leading=True
for ch in data:
    if leading and ch=="0":
        continue
    else:
        leading = False
        ndata+=ch
        
data=ndata
for i in range(1, len(data)):
    d1=data[:i]
    d2=data[i:]
    if d2[0]!="0":
        exps.append([d1, d2])
        for j in range(1, len(d2)):
            d3=d2[:j]
            d4=d2[j:]
            if d4[0]!="0":
                exps.append([d1, d3, d4])
                for k in range(1, len(d4)):
                    d5=d4[:k]
                    d6=d4[k:]
                    if d6[0]!="0":
                        exps.append([d1, d3, d5, d6])
print(exps)  
ans=0
for e in exps:
    if len(e)==2:
        ans+=check2(e)
    elif len(e)==3:
        ans+=check3(e)
    elif len(e)==4:
        ans+=check4(e)
print(ans)
                