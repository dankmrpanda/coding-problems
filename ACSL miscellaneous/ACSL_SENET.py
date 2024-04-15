data = "3, 24, 28, 16, 4, 1, 25, 26, 4, 4"
data = list(map(int, data.split(", ")))

n=data[0]
b=data[1:n+1]
m=data[n+1]
w=data[n+2:m+n+2]
rod=data[-1]
a=True

if b[0]==27 and rod==4:
    print("DONE")
elif b[0]+rod==27 and 15 in b==True:
    b[0]=27
    print(b[0])
elif b[0]+rod==27:
    b[0]=15
    print(b[0])
elif b[0]==27 and rod!=4:
    print("CANNOT MOVE")
elif b[0]==28 and rod==3:
    print("DONE")
elif b[0]==28 and rod!=3:
    print("CANNOT MOVE")
elif b[0]==29 and rod==2:
    print("DONE")
elif b[0]==29 and rod!=2:
    print("CANNOT MOVE")
elif b[0]<26 and b[0]+rod>26:
    b[0]=26
    print(b[0])
elif a==True:
    for i in range(len(b)):
        if b[0]+rod==b[i]:
            print("CANNOT MOVE")
            break
    else:   
        print(b[0]+rod)