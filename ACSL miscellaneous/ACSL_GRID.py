def num2ij(n):
    j=(n-1)%5
    i=abs((n-1)//5-4)
    return i,j

def ij2num(i,j):
    return(21-i*5)+j

def checkType(type):
    for i in range(4,-1,-1):
        for j in range(5):
            if type==1:
                if grid[i][j]:
                    grid[i][j]=False
                    num=ij2num(i,j)
                    return num
            elif type==2:
                if i>=1 and grid[i][j] and grid[i-1][j]:
                    grid[i-1][j]=False
                    num=ij2num(i,j)
                    return num
            elif type==3:
                if i>=3 and grid[i][j] and grid[i][j+1]:
                    grid[i][j]=False
                    grid[i-1][j]=False
                    num=ij2num(i,j)
                    return num
                

#grid =[[True]*5]*5
grid=[[True for i in range(5)] for i in range(5)]

num2ij(21)

data="8, 1, 3, 5, 6, 7, 8, 10, 13"
data=[int(i) for i in data.split(", ")]

for n in data:
    i,j=num2ij(n)
    grid[i][j]=False

types=[1,1,2,3,2]
for t in types:
    num=checkType(t)
    print(num)