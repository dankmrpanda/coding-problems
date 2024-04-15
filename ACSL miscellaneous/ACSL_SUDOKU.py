from os import path

curr_dir=path.dirname(__file__)


file = open("sudoku.txt", 'r')
ofile=open("sudoku_out.txt", "w")

#L1 = file.readline()
#L1=list(map(int,L1.readline().strip().split(",")))

#for line in file:
#   print(line)

N=int(file.readline())

sudoku = []
for i in range(N):
    line = list(map(int, file.readline().strip().split(",")))
    sudoku.append(line)
    print(line, file=ofile)

M=int(file.readline())
pos = []
for i in range(M):
    line = list(map(int, file.readline().strip().split(",")))
    pos.append(line)
    print(line, file=ofile)
print(sudoku)
print(pos)

file.close()
ofile.close()