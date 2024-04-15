def rc2ij(r,c):
    j=c-1
    i=abs(r-5)
    return i,j
data = "3, 3, 2"

N=5

grid=[[True for i in range(N)] for j in range(N)]

data=[int(i) for i in data.split(", ")]
qr, qc=data[0:2]
n=data[-1]

qi,qj=rc2ij(qr,qc)

qL=max(0, qj-n)
qR=min(4, qj+n)
qT=max(0, qi-n)
qB=min(4, qi+n)

for i in range(5):
    for j in range(5):
        if (qL<=j<=qR and i==qi) or (qT<=i<=qB and j==qj) or \
            (qL<=j<=qR and qT<=i<=qB and qi+qj==i+j) or \
            (qL<=j<=qR and qT<=i<=qB and qi+qj==i-j):
                grid[i][j]=False
ans=0
for row in grid:
    ans+=sum(row)
print(ans)
# temp=0
# qq=1
# ww=1
# ee=1
# rr=1

# if data[2]+data[0]>5:
#     q=data[2]+data[0]
#     qq=q-5
        
# if data[0]-data[2]<1:
#     w=data[0]-data[2]
#     ww=w+1
#     ww=ww*-1
    
# if data[1]-data[2]<1:
#     e=data[1]-data[2]
#     ee=e+1
#     ee=ee*-1
    
# if data[1]+data[0]>5:
#     r=data[1]+data[0]
#     rr=r-5
    
# t=data[0]+data[2]
# tt=data[1]+data[2]

# total=tt*t

# a=qq*ww
# b=ee*rr

# total=total-a
# total=total-b
# print(total)