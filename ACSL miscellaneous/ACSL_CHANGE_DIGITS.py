data=587
data = str(data)
num=[]
for i in data:
    i=int(i)
    num.append(i)
    
mean=0
times=0
for i in num:
    mean+=i
    times+=1

mean=mean//times
index=0
closest=9
for i in range(len(num)-1):
    if abs(num[i]-mean)==0:
        closest=num[i]
        index=i
        break
    elif abs(num[i]) < closest:
        closest=num[i]
        index=i

if closest==0 or closest==1 or closest==2:
    numm=[]
    for i in num:
        numm.append(i)
    numm.sort()
    num[index]=numm[-1]
    
elif closest==3 or closest==4 or closest==5:
    numm=[]
    for i in num:
        numm.append(i)
    numm.sort()
    num[index]=numm[0]
    
elif closest==6 or closest==7 or closest==8:
    summ=0
    for i in num:
        summ+=i
    if summ>9:
        num[index]=summ%10
    else:
        num[index]=summ
        
elif closest==9:
    num[index]=0

end=""
for i in num:
    i=str(i)
    end=end+i
end=int(end)
print(end)

