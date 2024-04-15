#http://www.usaco.org/index.php?page=viewproblem2&cpid=891

shell = [1, 2, 3]
count = [0, 0, 0]

f = open("shell.in")
n = int(f.readline())

for i in range(n):

    lst = list(map(int, f.readline().split()))
    a, b, g = lst[0]-1, lst[1]-1, lst[2]-1

    shell[a], shell[b] = shell[b], shell[a]

    count[shell[g]-1] += 1

with open("shell.out", "w") as d:
    d.write(str(max(count)))