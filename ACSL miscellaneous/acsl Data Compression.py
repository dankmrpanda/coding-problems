import re
import string

lst="THE PLACE TO BE HAPPY IS HERE; THE TIME TO BE HAPPY IS NOW."
lst=re.findall(r"[\w']+|[.,!?;]", lst)
for i in range(len(lst)):
    if lst[i] in string.punctuation:
        temp=lst[i]
        lst.pop(i)
        lst.append(temp)
final=[]
for i in range(len(lst)):
    count=0
    for x in range(len(lst)):
        if lst[i]==lst[x]:
            count+=1
            
    q=True
    for z in final:
        if (str(count)+lst[i])==z:
            q=False
            break
    if q==True:
        final.append(str(count)+lst[i])

testing="2THE1PLACE2TO2BE2HAPPY2IS1HERE1TIME1NOW1;1."
print("".join(final)==testing)           