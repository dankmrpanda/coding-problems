data1="2, 3, 4, 2, 3, 4"
data = list(map(float ,data1.split(", ")))
tri=[data[1], data[2], data[0]]
tri1=[data[4], data[5], data[3]]
# c=data[0]
# a=data[1]
# b=data[2]
# f=data[3]
# d=data[4]
# e=data[5]
tri11=["D", "E", "F"]
final=""

for i in range(3):
    for x in range(3):
        if tri1[x]==tri[i]:
            tri11[x]=str(tri11[x])
            final+=tri11[x]
            
if (len(final)!=3):
    final="NONE"
    
print(final)