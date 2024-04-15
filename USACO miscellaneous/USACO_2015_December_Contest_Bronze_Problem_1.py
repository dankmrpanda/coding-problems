file =open("paint.in", 'r')
#file =open("paint.in.txt", 'r')
farmer = list(map(int, file.readline().split()))
cow=list(map(int, file.readline().split()))

fr=list(range(farmer[0], farmer[1]+1))
cr=list(range(cow[0], cow[1]+1))

for i in fr:
    cr.append(i)
cr=[*set(cr)]
cr.sort()
with open("paint.out", "a") as o:
    e=str(cr[-1]-cr[0])
    o.write(e)