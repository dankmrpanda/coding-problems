colors = [c1, c2, c3, c4, c5]
fib = [1,1,2,3,5]

i=0
for c in colors: 
    if c=="R":
        pass
    elif c=="G":
        pass
    elif c=="B":
        pass
    i+=1
    
colors = "GGBWG"

for i,c in enumerate(colors):
    print(i,c)
    
for i in range(5):
    if colors[i]=="R":
        pass
    
# 01:02
h,m=1,2

print("{:02}:{:02}".format(h,m))

# "100,101,102,103"

p=["100","101","102","103"]
#p=[1,2,3,4]
",".join(p)

ans = ""

for i in range(100,104):
    ans+=","+str(i)
print(ans)