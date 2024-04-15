def figS(h, n=1):
    for i in range(h):
        r1="*"*h
        r2=r1[1:]
        r=r1+r2*(n-1)
        print(r)
        
def figH(h, n=1):
    for i in range(h):
        r1="*"*(h-i)+" "*i
        r2=r1[1:]
        r=r1+r2*(n-1)
        print(r)

def figL(h, n=1):
    for i in range(h):
        r1="*"*i + " "*(h-i)
        r2=r1[:-1]
        r=r2*(n-1)+r1
        print(r)

def figB(l,w, n=1):
    for i in range(w):
        r1="*"*l
        r2=r1[1:]
        r=r1+r2*(n-1)
        print(r)
        
def figT(h, n=1):
    r1=" "*(h-1)+"*"*h+" "*(h-1)
    r2="*"*(h-1)+"*"*h+"*"*(h-1)
    r1p =r1[1:]
    r2p=r2[1:]
    
    long = [h,h+(h-1)]
    for i in range(1,(3*h-1)):
        if i not in long:
            r=r1+r1p*(n-1)
        else:
            r=r2+r2p*(n-1)
        print(r)

inf=open("asterisks_data.txt",'r')
type=["H", "S", "L", "B", "T"]
func=[figH, figS, figL, figB, figT]

for line in inf:
    data=line.strip().split(",")
    if data[0]=="B":
        l=int(data[1])
        w=int(data[2])
        n=int(data[3])
        f=func[type.index(data[0])]
        f(1,w,n)
    else:
        h=int(data[1])
        n=int(data[2])
        
        f=func[type.index(data[0])]
        f(h,n)
    print()

inf.close()