data="196, 10"
data=data.split(", ")
num=int(data[0])
base=int(data[1])

def tobase10(n, b):
    n=[int(d) for d in str(n)]
    p=len(n)-1
    ans=0;
    for i in range(len(n)):
      ans+=n[i]*(pow(b, p))
      p-=1
    return ans

def base10to(n, b):
    ans=''
    summ=n
    while(summ!=0):
      x=summ%b
      summ=summ//b  
      ans=str(x)+ans
    return int(ans)

count=0
while count!=10:
    reverse=int(str(num)[::-1])
    dnum=tobase10(num, base)+tobase10(reverse, base)
    num=base10to(dnum, base)
    # print(num)
    if num==int(str(num)[::-1]):
        break
    count+=1
    
if(count==10):
    print("NONE, "+str(num))
else:
    print(num)      