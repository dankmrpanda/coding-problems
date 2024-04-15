import urllib
file = urllib.request.urlopen("http://www.datafiles.acsl.org/2020/contest1/int-sample-input.txt")
for line in file:
    data1 = line.decode("utf-8")
    data=list(map(str,data1.split()))
    n=data[0]
    p=int(data[1])
    pp=n[len(n)-p]
    left=n[:len(n)-p]
    right=n[(len(n)-p)+1:]
    leftf=""
    rightf=""
    for i in range(len(left)):
        u=(int(left[i])+int(pp))%10
        u=str(u)
        leftf+=u

    for i in range(len(right)):
        e=abs(int(right[i])-int(pp))
        e=str(e)
        rightf+=e
    
    final=""
    final+=leftf
    final+=pp
    final+=rightf
    print(final)
