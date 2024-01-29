#http://www.usaco.org/index.php?page=viewproblem2&cpid=665

inputs = []
with open("cowsignal.in", "r") as f:
    inputs = f.read().split("\n")

num = int(inputs[0].split()[2])
x = int(inputs[0].split()[0])
y = int(inputs[0].split()[1])
inputs.pop(0)
with open("cowsignal.out", "w") as f:
    for i in range(x * num): #i height of the line
        for z in range(y * num): #z width of the line
            print(inputs[i // num][z // num], end="", file=f) 
        print(file=f)