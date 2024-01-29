lines = list(map(int, input().split())) #[0] = cow num, [1] = candy num
cows = list(map(int, input().split()))
candy = list(map(int, input().split()))

for i in range(lines[1]): #loops thru all candys
    candynum = candy[i]
    eaten = 0
    for x in range(lines[0]): #loops thru all cows
        if candynum <= 0: #ends early if all candy is eaten
            break
        if cows[x] > eaten: #if the cow's height is greater than the amount of candy eaten
            ogval = cows[x] - eaten #gets the max possible candy to eat
            cows[x] += ogval #presets max cow height, will readjust later
            candynum -= ogval #deletes the max eat from candy left 
            if candynum < 0: #if its negative then that means cow ate more than there is, readjust by deleting excess
                cows[x] -= (candynum * -1)
                candynum = 0
            eaten += cows[x] - (ogval + eaten) #update eaten value
for i in cows:
    print(i)