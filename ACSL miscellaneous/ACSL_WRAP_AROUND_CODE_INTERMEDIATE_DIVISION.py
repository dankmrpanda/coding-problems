data="A,C,S,L,$"
data=list(data.split(","))
data.remove("$")
for i in range(len(data)):
    data[i]=data[i].lower()
numlist = [ord(x) - 96 for x in data]
final=[]
last=1
a=0
b=0

for i in range(len(numlist)):
    if numlist[i]>=1 and numlist[i]<=5:
        count=numlist[i]*2
    elif numlist[i]>=6 and numlist[i]<=10:
        count=numlist[i]%3
        count=count*5
    elif numlist[i]>=11 and numlist[i]<=15:
        count=numlist[i]//4
        count=count*8
    elif numlist[i]>=16 and numlist[i]<=20:
        a=numlist[i]//10
        b=numlist[i]%10
        count=(a+b)*10
    elif numlist[i]>=21 and numlist[i]<=26:
        for x in range (numlist[i], 0, -1):
            if numlist[i] % x == 0:
                count=x
                break
            break
        count=count*12
    last+=count%26
    last=last%26
    final.append(last)

for x in range(len(final)):
    final[x]=chr(final[x]+96)
    
for i in range(len(final)):
    final[i]=final[i].upper()
print(" ".join(final))
