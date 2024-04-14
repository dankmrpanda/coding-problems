data = "9 3 141 5926 535 89 72 3 846 26 43 383 27"
lst = list(map(int, data.split()))
num = lst.pop(0)
llst = lst.copy()
ascend = True
nlst = []

for i in range(num, 0, -1):
    if len(llst) < i:
        llst += lst
    alst = llst[:i]
    del llst[:i]
    if ascend:
        ascend = False
        alst.sort()
    else:
        ascend = True
        alst.sort(reverse= True)
    nlst += alst

if len(llst) != 0:
    if ascend:
        llst.sort()
    else:
        llst.sort(reverse= True)
    nlst += llst

print(*nlst)