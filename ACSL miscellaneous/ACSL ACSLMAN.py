data="BIT, 11, A,C,D,E,F,G,H,J,K,L,M"
data=data.replace(" ", "").split(",")
word=[i for i in data[0]]
data.pop(0)
data.pop(0)

count=0
man=[[" ", " ", "O", " ", " "], 
     ["+", "=", "[]", "=", "+"],
     [" ", " ", "[]", " ", " "],
     [" ", "/", "\\", " ", " "]]
for i in range(len(word)):
    for x in range(len(data)):
        if count==9:
            break
        if word[i]==data[x]:
            #for printing the thing, just do count and if the index is blank, dont minus 1 and also print it
            