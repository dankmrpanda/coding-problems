data="IN A RIGHT TRIANGLE THE SQUARE OF THE HYPOTENUSE EQUALS THE SUM OF THE SQUARES OF THE LEGS"

def q1():
    wordcount=len(data.split())
    print(wordcount)

def q2():
    x=data.replace(" ","* *")
    wordreverselist=x.split("*")
    wordreverse=''.join(i[::-1] for i in wordreverselist)
    print(wordreverse)
    
def q3():
    words=data.split()
    end=[]
    for i in range(len(words)):
        if end.count(words[i])==0:
            end.append(words[i])
    end.sort()
    for i in range(len(end)):
        print(end[i], end=" ")
    print()

def q4():
    l1=[]
    l1[:0]=data
    end=[]
    for i in range(len(l1)):
        if end.count(l1[i])==0 and l1[i]!=" ":
            end.append(l1[i])
    end.sort()
    for i in range(len(end)):
        print(end[i], end="")
    print()
    
def q5():
    words=data.split()
    words.reverse()
    print(*words, sep=" ")
    
q1()
q2()
q3()
q4()
q5()