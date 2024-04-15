#http://www.usaco.org/index.php?page=viewproblem2&cpid=855

f = open("mixmilk.in")
inputs = f.read().split()
inputs = list(map(int, inputs))

maxx = [inputs[0], inputs[2], inputs[4]]
start = [inputs[1], inputs[3], inputs[5]]

for i in range(100):
    if i % 3 == 0:
        added = start[0] + start[1]
        if added > maxx[1]:
            start[0] = added - maxx[1]
            start[1] = maxx[1]
        else:
            start[0] = 0
            start[1] = added
    elif i % 3 == 1:
        added = start[1] + start[2]
        if added > maxx[2]:
            start[1] = added - maxx[2]
            start[2] = maxx[2]
        else:
            start[1] = 0
            start[2] = added
    elif i % 3 == 2:
        added = start[2] + start[0]
        if added > maxx[0]:
            start[2] = added - maxx[0]
            start[0] = maxx[0]
        else:
            start[2] = 0
            start[0] = added
print(str(start[0]) + "\n" + str(start[1]) + "\n" + str(start[2]), file=open("mixmilk.out", "w"))