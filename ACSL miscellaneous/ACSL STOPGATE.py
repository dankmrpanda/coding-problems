data="L, 5, 3, 3, 4, 5, 5, 1, 6, 2, 8, 1, 3, 7, 5, 4, 5, 6, 5, 8, 7, 4"

direction=data[0]
LR=False
if direction=="L":
    LR=True
data=[int(i) for i in data[3:].split(", ")]

print(direction,data)

board =[[False for i in range(8)] for i in range(8)]
N=data[0]

for i in range(N):
    row=data[1+2*i]
    col=data[2+2*i]
    br=8-row
    bc=col-1
    board[br][bc]= True
    if LR:
        board[br][bc+1]=True
    else:
        board[br-1][bc]=True
    
LR=not LR
for i in range(N):
    row=data[1+2*i]
    col=data[2+2*i]
    br=8-row
    bc=col-1
    board[br][bc]= True
    if LR:
        board[br][bc+1]=True
    else:
        board[br-1][bc]=True
LR=not LR

count=0
for r in range(8):
    for c in range (8):
        if LR:
            if c<7 and board[r][c]==False and board[r][c+1]==False:
                count+=1
        else:
            if c>0 and board[r][c]==False and board[r-1][c]==False:
                count+=1

print(count)