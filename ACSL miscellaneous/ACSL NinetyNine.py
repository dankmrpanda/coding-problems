data1 = "75, 7, 3, 8, 8, 7, T, 5, 9, A, 6"
data = list(map(str, data1.split(", ")))
for i in range(len(data) - 1):
    try:
        int(data[i])

        data[i] = int(data[i])
    except ValueError:
        continue
starting = data[0]
# starting = x
counter = 0
go = 4
dic = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

deck = [data[1], data[2], data[3]]
deck1 = [data[5], data[7], data[9]]
# print(deck1)
for i in range(len(deck1)):
    if (
        deck1[i] == "T"
        or deck1[i] == "J"
        or deck1[i] == "Q"
        or deck1[i] == "K"
        or deck1[i] == "A"
    ):
        deck1[i] = dic[deck1[i]]
# print(deck1)

while starting <= 99:
    if counter % 2 == 0:
        for i in range(len(deck)):
            if (
                deck[i] == "T"
                or deck[i] == "J"
                or deck[i] == "Q"
                or deck[i] == "K"
                or deck[i] == "A"
            ):
                deck[i] = dic[deck[i]]

        deck.sort()
        # print(deck)
        # print(deck[-1])
        if deck[-1] == 14:
            if starting + 14 <= 99:
                starting += 14
            else:
                starting += 1
        elif deck[-1] == 10:
            starting -= 10
        elif deck[-1] == 9:
            starting += 0
        else:
            starting += deck[-1]
        del deck[-1]
        # print(deck)
        # print(str(starting)+"p")

    else:
        deck.append(data[go])
        go += 2
        # print(deck1)
        if len(deck1) != 0:
            if deck1[0] == 14:
                if starting + 14 <= 99:
                    starting += 14
                else:
                    starting += 1
            elif deck1[0] == 10:
                starting -= 10
            elif deck1[0] == 9:
                starting += 0
            else:
                starting += deck1[0]
            del deck1[0]
        # print(str(starting)+"d")
    counter += 1

if counter % 2 == 0:
    print(str(starting) + ", Player")
else:
    print(str(starting) + ", Dealer")
