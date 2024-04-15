n=int(input())
nums=input()
# n=4
# nums="1 6 4 6"
nums=list(map(int, nums.split()))
nums.sort(reverse=True)

maxx=0
maxt=0

for x in range(n):
    m=nums[x]*(x+1)
    if m>=maxx:
        maxx=m
        maxt=nums[x]
print(str(maxx) + " " + str(maxt))