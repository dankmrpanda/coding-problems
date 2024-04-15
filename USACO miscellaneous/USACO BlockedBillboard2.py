#https://usaco.org/index.php?page=viewproblem2&cpid=783

inf, outf = open("billboard.in"), open("billboard.out", "w")

x1, y1, x2, y2 = map(int, inf.readline().split())
x3, y3, x4, y4 = map(int, inf.readline().split())

x = [0, x1, x2, x3, x4]
y = [0, y1, y2, y3, y4]

if x[4] >=x[2] and x[3]<=x[1] and y[4]>= y[2] and y[3] <=y[1]:
	print(0,file=outf)
elif x[3] <= x[1]and y[3]<= y[1]and y[4] > y[1] and x[4]>= x[2]:
	print(str((x[2] - x[1]) * (y[2] - y[4])),file=outf)
elif y[3] < y[2] and x[3]<= x[1] and y[4] >= y[2] and x[4] >= x[2]:
	print(str((x[2] - x[1]) *(y[3] - y[1])),file=outf)
elif x[4]> x[1] and x[3] <= x[1] and y[4]>= y[2] and y[3] <= y[1]:
	print(str((x[2]- x[4]) * (y[2] -y[1])),file=outf)
elif x[3] < x[2] and x[4] >= x[2] and y[4] >= y[2] and y[3] <= x[1]:
	print(str((x[3]- x[1])* (y[2] -y[1])),file=outf)
else:
	print(str((x[2] -x[1]) *(y[2] - y[1])),file=outf)
    
inf.close()
outf.close()