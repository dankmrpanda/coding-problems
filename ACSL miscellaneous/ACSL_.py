waveLength=6
numbers="3 1 4 1 5 9 2 6"
num=numbers.split()
num=map(int, num)
num=list(num)
ending=[]
acsending=[]
desending=[]
count=0
pev=waveLength
for i in range(waveLength, 0, -1):
    if count%2==0:
        acsending.append(num[0:waveLength])
        acsending=[x for i in acsending for x in i ]
        acsending=sorted(acsending)
        print(acsending)
        del num[0:waveLength]
        
        if len(acsending)!=waveLength:
            print("acsending")
            print(acsending)
            print(len(acsending))
            print(waveLength)
            num=numbers.split()
            num=map(int, num)
            num=list(num)
            
            temp=[]
            temp.append(num[0:waveLength-len(acsending)])
            print(temp)
            for i in temp:
                temp=" ".join(map(str, i))
            print("tempp")
            print(temp)
            acsending="".join(str(temp))
            acsending=sorted(acsending)
            del num[0:waveLength]
            print(acsending)
            acsending="".join(str(temp))
            print(acsending)
            ending.append(acsending)
            waveLength=pev
            
        else:
            ending.append(acsending)
        acsending = []
        
    if count%2==1:
        desending.append(num[0:waveLength])
        desending=[x for i in desending for x in i ]
        desending=sorted(desending, reverse=True)
        print(desending)
        del num[0:waveLength]
        
        if len(desending)!=waveLength:
            print("desending")
            print(desending)
            print(len(desending))
            
            print(waveLength)
            num=numbers.split()
            num=map(int, num)
            num=list(num)
            temp=[]
            temp.append(num[0:waveLength-len(desending)])
            temp=[x for i in temp for x in i ]
            temp=sorted(temp)
            del num[0:waveLength]
            print(temp)
            desending="".join(str(temp))
            print(desending)
            ending.append(desending)
            waveLength=pev
            
            
        else:
            ending.append(desending)
            
        desending =[]
    print(ending)
    waveLength=waveLength-1
    
    
    if waveLength==0 and len(num)!=0:
        count=count-1
        print(count)
        if count%2==0:
            print("none left acsend")
            acsending.append(num[0:len(num)])
            acsending=[x for i in acsending for x in i ]
            acsending=sorted(acsending)
            ending.append(acsending)
            del num[0:waveLength]
            acsending =[]
            
        if count%2==1:
            print("none left desend")
            desending.append(num[0:len(num)])
            
            desending=[x for i in desending for x in i ]
            desending=sorted(desending, reverse=True)
            ending.append(desending)
            del num[0:len(num)]
            desending =[]
        break
    count=count+1
    print("loop done")
    
final=[x for i in ending for x in i ]
total=" ".join(str(e) for e in final)
print(total)


# if len(desending)!=0:
#     if len(desending)!=waveLength:
#         print(desending)
#         print(len(desending))
        
#         print(waveLength)
#         num=numbers.split()
#         num=map(int, num)
#         num=list(num)
#         waveLength=pev
#         print("d")
#         desending =[]
# elif len(acsending)!=0:
#     if len(acsending)!=waveLength:
#         print(acsending)
#         print(len(acsending))
        
#         num=numbers.split()
#         num=map(int, num)
#         num=list(num)
#         waveLength=pev
#         print("a")
#         acsending =[]
# else:
#     ending.append(desending)
#     ending.append(acsending)
    
    # desending =[]
    # acsending =[]