data="5, 0, 6, 6, 0, 4"
data = [int(s) for s in data.split(", ")]

moves=0

def lastOccuranceIndex(lst, num):
    lst.reverse()
    d=lst.index(num)
    r=len(lst) - d - 1
    lst.reverse()
    return r

while len(data)!=0:
    #print(data) 
    moves+=1
    status=0
    counter=0
    num=data[0]
    
    for i in range(len(data)):
        if data[i]==0:
            # data.reverse()
            # d=data.index(0)
            # r=len(data) - d - 1
            # data.reverse()
            del data[0:lastOccuranceIndex(data, 0)+1]
            status=1
            break
        
        f=data.count(i)
        if f>counter:
            counter=f
            num=i
        elif f==counter and i>num:
            num=i
    
    if status !=1:
        # data.reverse()
        # ind=data.index(num)
        # righti=len(data) - ind - 1
        # data.reverse()
        righti=lastOccuranceIndex(data, num)
        
        if data[righti]%2==0:
            data[righti]-=2
        else:
            data[righti]-=1
            
print(moves)