data="H, ATKQJN, TJ, AQJ, ATKQJ"
data=data.split(", ")

trump=data[0]
dia=[*data[1]]
club=[*data[2]]
spade=[*data[3]]
heart=[*data[4]]


def case1(trump, dia, club, spade, heart):
    trumplist=[]
    if trump=="D":
        trumplist=dia
    elif trump=="C":
        trumplist=club
    elif trump=="S":
        trumplist=spade
    else:
        trumplist=heart
    if trumplist.count("A")>=2 and trumplist.count("K")>=2 and trumplist.count("Q")>=2 and trumplist.count("J")>=2 and trumplist.count("T")>=2:
        return 150
    return 0

def case2(dia, spade):
    if dia.count("J")>=2 and spade.count("Q")>=2:
        return 30
    return 0

def case3(dia, club, spade, heart):
    if dia.count("A")>=1 and club.count("A")>=1 and spade.count("A")>=1 and heart.count("A")>=1:
        return 10
    return 0

def case4(dia, club, spade, heart):
    if dia.count("K")>=1 and club.count("K")>=1 and spade.count("K")>=1 and heart.count("K")>=1:
        return 8
    return 0

def case5(dia, club, spade, heart):
    if dia.count("A")>=2 and club.count("A")>=2 and spade.count("A")>=2 and heart.count("A")>=2:
        return 100
    return 0

def case6(dia, club, spade, heart):
    if dia.count("K")>=2 and club.count("K")>=2 and spade.count("K")>=2 and heart.count("K")>=2:
        return 80
    return 0

def case7(trump, dia, club, spade, heart):
    n1=[]
    n2=[]
    n3=[]
    if trump=="D":
        n1=club
        n2=spade
        n3=heart
    elif trump=="C":
        n1=dia
        n2=spade
        n3=heart
    elif trump=="S":
        n1=club
        n2=dia
        n3=heart
    else:
        n1=club
        n2=spade
        n3=dia
    countt=0
    if(n1.count("A")>=1 and n1.count("K")>=1 and n1.count("Q")>=1 and n1.count("J")>=1 and n1.count("T")>=1):
        countt+=50
    if(n2.count("A")>=1 and n2.count("K")>=1 and n2.count("Q")>=1 and n2.count("J")>=1 and n2.count("T")>=1):
        countt+=50
    if(n3.count("A")>=1 and n3.count("K")>=1 and n3.count("Q")>=1 and n3.count("J")>=1 and n3.count("T")>=1):
        countt+=50
    return countt

def case8(dia, spade):
    if(dia.count("J")>=1 and spade.count("Q")>=1):
        return 4
    return 0

def case9(dia, club, spade, heart):
    if dia.count("Q")>=1 and club.count("Q")>=1 and spade.count("Q")>=1 and heart.count("Q")>=1:
        return 6
    return 0

def case10(dia, club, spade, heart):
    if dia.count("J")>=1 and club.count("J")>=1 and spade.count("J")>=1 and heart.count("J")>=1:
        return 4
    return 0

def case11(dia, club, spade, heart):
    if dia.count("Q")>=2 and club.count("Q")>=2 and spade.count("Q")>=2 and heart.count("Q")>=2:
        return 60
    return 0

def case12(dia, club, spade, heart):
    if dia.count("J")>=2 and club.count("J")>=2 and spade.count("J")>=2 and heart.count("J")>=2:
        return 40
    return 0


count=0
count+=case1(trump, dia, club, spade, heart)
count+=case2(dia, spade)
count+=case3(dia, club, spade, heart)
count+=case4(dia, club, spade, heart)
count+=case5(dia, club, spade, heart)
count+=case6(dia, club, spade, heart)
count+=case7(trump, dia, club, spade, heart)
count+=case8(dia, spade)
count+=case9(dia, club, spade, heart)
count+=case10(dia, club, spade, heart)
count+=case11(dia, club, spade, heart)
count+=case12(dia, club, spade, heart)
print(count)