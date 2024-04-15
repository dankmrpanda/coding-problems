file =open("cowsignal.in", 'r')

data = list(map(int, file.readline().strip().split()))
datax=[]
end=[]
for i in range(data[0]):
    datax.append(list(file.readline()))

for i in range(data[0]):
    string=""
    for y in datax[i]:
        string += y
    for x in range(data[1]):
        ess="".join([x*data[2] for x in string])
    for x in range(data[2]):
        end.append(ess)
endd=[]
for x in end:
    endd.append(x.replace("\n", ""))

with open("cowsignal.out", "a") as o:
    for i in range(len(endd)):
        o.write(endd[i]+"\n")