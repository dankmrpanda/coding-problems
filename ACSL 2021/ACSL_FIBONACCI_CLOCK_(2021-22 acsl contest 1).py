data = "B, B, B, B, B"
data = data.split(", ")
c1 = data[0]
c2 = data[1]
c3 = data[2]
c4 = data[3]
c5 = data[4]


def findTime(c1, c2, c3, c4, c5):
    mins = 0
    hours = 0
    R = 0
    B = 0
    G = 0

    if c1 == "R":
        R = R+1
    elif c1 == "B":
        B = B+1
    elif c1 == "G":
        G = G+1

    if c2 == "R":
        R = R+1
    elif c2 == "B":
        B = B+1
    elif c2 == "G":
        G = G+1

    if c3 == "R":
        R = R+2
    elif c3 == "B":
        B = B+2
    elif c3 == "G":
        G = G+2

    if c4 == "R":
        R = R+3
    elif c4 == "B":
        B = B+3
    elif c4 == "G":
        G = G+3

    if c5 == "R":
        R = R+5
    elif c5 == "B":
        B = B+5
    elif c5 == "G":
        G = G+5

    hours = R+B
    mins = (G+B)*5

    if mins >= 60:
        temp = mins/60
        temp = int(temp)
        hours = hours+temp
        temps = temp*60
        mins = mins-temps

    if hours >= 12:
        hours = hours-12

    if hours <= 9:
        hours = str(hours)
        hours = "0"+hours
    if mins <= 9:
        mins = str(mins)
        mins = "0"+mins

    mins = str(mins)
    hours = str(hours)
    return hours+":"+mins


print(findTime(c1, c2, c3, c4, c5))
