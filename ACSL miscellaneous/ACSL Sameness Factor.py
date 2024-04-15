import urllib.request

file="http://www.datafiles.acsl.org/2020/contest2/int-sample-input.txt"
with urllib.request.urlopen(file) as f:
    html = f.read().decode('utf-8')
lst=html.split("\n")

var=["lst1", "lst2", "lst3", "lst4", "lst5"]

for n in range(5):
    exec(f"{var[n]}=lst[n]")


def asf(lst):
    p=lst.split()
    p1=[*p[0]]
    p2=[*p[1]]
    
    i=0
    length=0
    if(len(p1)<len(p2)):
        length=len(p1)
    else:
        length=len(p2)
        
    while(True):
        
    
    
    
    
    
    # length=0
    
    # np1=[]
    # np2=[]
    # if(len(p1)<len(p2)):
    #     length=len(p1)
    #     for i in range(length):
    #         if p1[i]!=p2[i]:
    #             np1.append(p1[i])
    #             np2.append(p2[i])

    #     for i in range(length, len(p2)):
    #         np2.append(p2[i])
        
    # else:
    #     length=len(p2)
    #     for i in range(length):
    #         if p1[i]!=p2[i]:
    #             np1.append(p1[i])
    #             np2.append(p2[i])
            
    #     for i in range(length-1, len(p1)):
    #         np2.append(p1[i]) 
    # print(np1)
    # print(np2)

slst="ABCDEFT ABXCGBTZFP"
asf(slst)