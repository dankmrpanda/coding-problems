data1="12,1,1,1,4,1,7,2,1,3,4,4,5,5,3,5,6,6,2,6,4,6,5,7,3"
data2="1, 3, 2, 2, 3"
test1="5, 2"
test2="7, 7"
test3="5, 6"
test4="1, 4"
test5="6, 4"

data1=data1.split(",")
data1 = [int(i) for i in data1]

cells=[]
for i in range(data1[0]):
    cells.append([data1[1], data1[2]])
    data1.pop(1)
    data1.pop(1)
data1.pop(0)


data2=data2.split(",")
data2 = [int(i) for i in data2]

birth=[]
for i in range(data2[0]):
    birth.append(data2[1])
    data2.pop(1)
data2.pop(0)

survive=[]
for i in range(data2[0]):
    survive.append(data2[1])
    data2.pop(1)
data2.pop(0)

test1=test1.split(",")
test1 = [int(i) for i in test1]

test2=test2.split(",")
test2 = [int(i) for i in test2]

test3=test3.split(",")
test3 = [int(i) for i in test3]

test4=test4.split(",")
test4 = [int(i) for i in test4]

test5=test5.split(",")
test5 = [int(i) for i in test5]

def maincalc(test):
    count=0
    x=test[0]
    y=test[1]
    status="D"
    for i in range(len(cells)):
        xx=cells[i][0]
        yy=cells[i][1]
        if(x-1==xx and y-1==yy):
            count+=1
        if(x==xx and y-1==yy):
            count+=1
        if(x+1==xx and y-1==yy):
            count+=1
        if(x-1==xx and y==yy):
            count+=1
        if(x+1==xx and y==yy):
            count+=1
        if(x-1==xx and y+1==yy):
            count+=1
        if(x==xx and y+1==yy):
            count+=1
        if(x+1==xx and y+1==yy):
            count+=1
        if(x==xx and y==yy):
            status="A"
    afters="D"
    if status=="D":
        for i in range(len(birth)):
            if count==birth[i]:
                afters="A"
    if status=="A":
        for i in range(len(survive)):
            if count==survive[i]:
                afters="A"
    print(status+", "+str(count)+", "+afters)
    
maincalc(test1)
maincalc(test2)
maincalc(test3)
maincalc(test4)
maincalc(test5)