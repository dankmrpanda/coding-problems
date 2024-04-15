#https://usaco.org/index.php?page=viewproblem2&cpid=987&authuser=0
inf, outf = open("word.in"), open("word.out", "w")
nk="billboard.in"
string = input().split()
k = int(nk.split()[1])
count = 0
for i in string:
    if count + len(i) >= k:
        print(i,file=outf)
        count = len(i)
    else:
        print(i,end=" ",file=outf)
        count+=len(i)

inf.close()