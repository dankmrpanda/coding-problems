def 

data="3,4,4,5,7,2,10,4,2,9,1,13,5,15,3,21,3,4,5"
data=[int(i) for i in data.split(",")]
n=data[0]
mine={}
for i in range(n):
    amount=data[1+(i*2)]
    loc=data[2+(i*2)]
    mine[loc]=amount
    
m=data[n*2+1]
enemy = {}
for i in range(m):
    amount =data[(2*n+2)+(i*2)]
    loc=data[(2*n+3)+(i+2)]
    enemy[loc]=amount
    
print(mine,enemy)       

rolls=data[-1:-4:-1]
print(rolls)

occupied=[]
for k,v in mine.items():    
    if v==5:
        occupied.append(k)

for k,v in enemy.items():
    if v>=2:
        occupied.append(k)

moves=3

if moves==3:
    count=0
    for i in rolls:
        if i not in occupied:
            count+=1
    if count==3:
        addToMine(rolls)
    else:
        moves-=1
elif moves==2:
    possible=[[sum(rolls[:2], rolls[2])]],
                [sum(rolls[1:]),rolls[0]],
                [rolls[0]+rolls[-1],rolls[1]]
    possible.sort(reverse=True)
    done=False
    for i in possible:
        if i[0] not in occupied and i[1] not in occupied:
            addToMine(i)
            done=True
            break
    if not done:
        moves-=1
        
elif moves==1:
    possible=sum(rolls)
    if possible not in occupied:
        addToMine([possible])
    else:
        move-=1
else:
    