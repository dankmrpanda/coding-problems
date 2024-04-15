data="8, A, D, D, A, D, D, A, A, 2"
data=data.split(", ")

n=int(data[0])
cells=data[1:n+1]

gen=int(data[-1])

cells=["D"]+cells+["D"]

for g in range(gen):
    ngen=cells.copy()
    for i in range(1, n+1):
        if (cells[i-1]=="A" and cells[i+1]=="D" or \
            cells[i-1]=="D" and cells[i+1]=="A"):
            ngen[i]="A"
        if (cells[i-1]=="A" and cells[i+1]=="A" or \
            cells[i-1]=="D" and cells[i+1]=="D"):
            ngen[i]="D"
    cells=ngen
print("".join(ngen[1:n+1]))