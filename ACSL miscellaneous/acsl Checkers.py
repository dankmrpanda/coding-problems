data="2, 4, 7, 3, 5, 5, 7, 7, 5, 7, 7, 5, 3, 4, 2, 3, 1"
data=data.split(", ")
data = [int(i) for i in data]
own=[data[0], data[1]]
numberc=data[2]
data.pop(0)
data.pop(0)
data.pop(0)
checkers=[]

for i in range(numberc):
    checkers.append([data[0], data[1]])
    data.pop(0)
    data.pop(0)
print(checkers)
final=0
for i in range(len(checkers)):
    count=0
    if own[0]!=8:
        for q in range(len(checkers)):
            if own[0]+1==checkers[q][0] and own[1]+1==checkers[q][1]:
                print("right up")
                for x in range(len(checkers)):
                    if own[0]+2==checkers[x][0] and own[1]+2==checkers[x][1]:
                        print("right up blocked")
                        break
                    count+=1
                if count==len(checkers) and own[0]+2<=8 and own[1]+2<=8:
                    print("right up done")
                    own=[own[0]+2, own[1]+2]
                    checkers.pop(0)
                    final+=1
                break
        
        
            elif own[0]+1==checkers[q][0] and own[1]-1==checkers[q][1]:
                print("left up")
                for x in range(len(checkers)):
                    if own[0]+2==checkers[x][0] and own[1]-2==checkers[x][1]:
                        print("left up blocked")
                        break
                    count+=1
                if count==len(checkers) and own[0]+2<=8 and own[1]-2<=8:
                    print("left up done")
                    own=[own[0]+2, own[1]-2]
                    checkers.pop(0)
                    final+=1
                break
    else:
        for q in range(len(checkers)):
            if own[0]-1==checkers[q][0] and own[1]+1==checkers[q][1]:
                print("right down")
                for x in range(len(checkers)):
                    if own[0]-2==checkers[x][0] and own[1]+2==checkers[x][1]:
                        print("right down blocked")
                        break
                    count+=1
                if count==len(checkers) and own[0]-2<=8 and own[1]-2<=8:
                    print("right up done")
                    own=[own[0]-2, own[1]+2]
                    checkers.pop(0)
                    final+=1
                break
        
        
            elif own[0]-1==checkers[q][0] and own[1]-1==checkers[q][1]:
                print("left down")
                for x in range(len(checkers)):
                    if own[0]-2==checkers[x][0] and own[1]-2==checkers[x][1]:
                        print("left down blocked")
                        break
                    count+=1
                if count==len(checkers) and own[0]-2<=8 and own[1]-2<=8:
                    print("left up done")
                    own=[own[0]-2, own[1]-2]
                    checkers.pop(0)
                    final+=1
                break
    print("checker is at: "+str(own[0])+" "+str(own[1]))
print(final)
