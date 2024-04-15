data1='623387770165388734 11'
data=list(map(str,data1.split()))
nums=data[0]
group=data[1]
group=int(group)
final=[]
while len(nums)>=group:
    fin=''
    for i in range(group):
        fin+=nums[i]
    nums=nums[1:]
    final.append(fin)
summ=0
for i in range(len(final)):
    summ+=int(final[i])
print(summ)