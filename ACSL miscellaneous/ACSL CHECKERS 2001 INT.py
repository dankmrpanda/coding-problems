def jump(curr,opp,king):
    px=curr[0]
    py=curr[1]
    
    for op in opp:
        if not king:
            if px+1==op[0] and py+1==op[1]:
                nx=op[0]+1
                ny=op[1]+1
                break
            elif px+1==op[0] and py-1==op[1]:
                nx=op[0]+1
                ny=op[1]-1
                break
        else:
            if px+1<=7 and py-1>=2 and px+1==op[0] and py-1==op[1]:
                nx=op[0]+1
                ny=op[1]-1
                break
            elif px+1<=7 and py+1<=2 and px+1==op[0] and py+1==op[1]:
                nx=op[0]+1
                ny=op[1]+1
                break
            elif px-1>=2 and py-1>=2 and px-1==op[0] and py-1==op[1]:
                nx=op[0]-1
                ny=op[1]-1
                break
            elif px-1>=2 and py+1<=7 and px-1==op[0] and py+1==op[1]:
                nx=op[0]-1
                ny=op[1]+1
                break
    return [nx,ny], op


data = "2, 2, 4, 3, 3, 5, 3, 7, 3, 7, 5"

data = [int(i) for i in data.split(", ")]

player=[data[0],data[1]]

N=data[2]

opp=[]

for i in range(N):
    opp.append([data[3+i*2],data[4+i*2]])

king=False
count=0

while len(opp)>0:
    if not king:
        king=player[0]==8
    
    newP, op=jump(player,opp,king)
    if newP!=player and newP not in opp:
        count+=1
        player=newP
        opp.remove(op)
    else:
        break
print(count)
    
#for op in opp:
#    if ((player[0]+1==op[0] and player[1]+1==op[1]) or (player[0]-1==op[0] and player[1]+1==op[1]) or (player[0]-1==op[0] and player[1]-1==op[1]) or (player[0]+1==op[0] and player[1]-1==op[1])):
#        score=score+1
        
        
    