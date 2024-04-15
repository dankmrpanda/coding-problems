def pops(num):
    num=int(num)
    for i in range(num):
        del lst[-1]

def pshs(letter):
    lst.append(letter)
    
def dups(num):
    for i in range(num-1):
        lst.append(lst[i])

def prt(num):
    for i in range(num):
        print(lst[i])
        
def popq(num):
    num=int(num)
    for i in range(num):
        del lst[0]

def pshq(letter):
    lst.insert(0, letter)
    
def dupq(num):
    for i in range(num-1):
        lst.insert(0, lst[i])
        

def s():
    for i in range(len(action)):
        if action[i]=="POP":
            pops(action[i+1])
        elif action[i]=="PSH":
            pshs(action[i+1])
        elif action[i]=="DUP":
            dups(action[i+1])
        elif action[i]=="SWH":
            break
        elif action[i]=="PRT":
            prt(action[i+1])
            
    
def q():
    for i in range(len(action)):
        if action[i]=="POP":
            popq(action[i+1])
        elif action[i]=="PSH":
            pshq(action[i+1])
        elif action[i]=="DUP":
            dupq(action[i+1])
        elif action[i]=="SWH":
            break
        elif action[i]=="PRT":
            prt(action[i+1])    





data = "S, POP 1, PRT 2"
data = list(map(str, data.split(", ")))
action=[]
lst=["A", "B", "C", "D", "E"]
for i in range(len(data)):
    temp=str(data[i])
    if " " in temp:
        s=temp.split();
        for j in range(len(s)):
            action.append(s[j])
            
if data[0]=="S":
    s()
else:
    q()