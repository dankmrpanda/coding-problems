inf = open("1.in", 'r')
outf=open("traffic.out", 'w')

N=int(inf.readline().strip())

traffics = []
for line in inf:
    seg=line.strip().split()
    seg[1]=int(seg[1])
    seg[2]=int(seg[2])
    traffics.append(seg)
print(traffics)

a,b=-99999999999999, 9999999999999
for i in traffics:
    if i[0]=="on":
        a-=i[2]
        b-=i[1]
        a=max(0, a)
    elif i[0]=="off":
        a+=i[1]
        b+=i[2]
    elif i[0]=="none":
        a=max(a, i[1])
        b=min(b, i[2])
print(a, b)

a,b=-99999999999999, 9999999999999
for i in traffics:
    if i[0]=="on":
        a+=i[1]
        b+=i[2]
    elif i[0]=="off":
        a-=i[2]
        b-=i[1]
        a=max(0, a)
    elif i[0]=="none":
        a=max(a, i[1])
        b=min(b, i[2])
print(a, b, file=outf)

inf.close()
outf.close()