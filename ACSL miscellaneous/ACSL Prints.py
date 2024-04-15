data="A, 2, 7, 8, 0"
data=list(data.split(", "))
for i in range(1, len(data)):
    data[i]=int(data[i])
h={10:1, 9:1, 8:2, 7:2, 6:4, 1:16, 2:16, 3:8, 4:8, 5:4}
a={1:16, 2:8, 3:4, 4:2, 5:1, 6:16, 7:8, 8:4, 9:2, 10:1}

if len(data)==2 and data[1]=='0':
    print("1/1")
    
elif data[0]=="H":
    even=1
    odd=1
    for i in range(1, len(data)-1):
        if data[i]%2==0:
            even+=h[data[i]]
        else:
            odd+=h[data[i]]
    print(str(even) + "/"+str(odd))
    
elif data[0]=="A":
    right=1
    left=1
    for i in range(1, len(data)-1):
        if data[i]>=6 and data[i]<=10:
            left+=a[data[i]]
        else:
            right+=a[data[i]]
    print(str(right) + "/"+str(left))