data=[18, 44, 7, 21, 23]
both=[]
for i in data:
    if i>=1 and i<=13:
        both.append("d")
        both.append(i%13)
    elif i>=14 and i<=26:
        both.append("h")
        both.append((i-13)%13)
    elif i>=27 and i<=39:
        both.append("s")
        both.append((i-26)%13)  
    elif i>=40 and i<=52:
        both.append("c")
        both.append((i-39)%13)

for i in range(len(data)):
    for j in range(i+2, len(data)-1, 2):
        if both[i+1]==both[j+1] and both[i]!=both[j]: