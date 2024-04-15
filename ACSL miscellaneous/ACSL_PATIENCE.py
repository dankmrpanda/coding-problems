data="4H"
data=data.split()
for i in range(len(data)):
    data[i]=[char for char in data[i]]

pile=[[[]]]
totallst=0
pilelst=0
pilelst2=0
for i in range(2):
    if data[i][0]=="4" and data[i][1]=="H":
        pile[pilelst][pilelst2][0].append(data[i][0])
        pile[pilelst][pilelst2][1].append(data[i][1])
piles={1:data[0]}