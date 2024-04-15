data = "10, 12, .4"
data = [float(i) for i in data.split(", ")]
l = data[0]
h = data[1]
t = data[2]

def solve(l, h, t): 
    if (l >= 3.5 and l <= 4.25) and (h >= 3.5 and h <= 6) and (t >= 0.007 and t <= 0.16):
        return "REGULAR POST CARD"
    elif (l > 4.25 and l < 6) and (h > 6 and h < 11.5) and (t >= 0.007 and t <= 0.16):
        return "LARGE POST CARD"
    elif (l >= 3.5 and l <= 6.15) and (h >= 5 and h <= 11.5) and (t > 0.016 and t < 0.25):
        return "ENVELOPE"
    elif (l > 6.125 and l < 24) and (h >= 11 and h <= 18) and (t >= 0.25 and t <= 0.5):
        return "LARGE ENVELOPE"
    elif ((l>=24 or h>18 or t > 0.5) and (l+2*(h+t) <= 84)):
        return "PACKAGE"
    elif ((l>=24 or h>18 or t > 0.5) and (l+2*(h+t) > 84 and l+2*(h+t) <= 130)):
        return "LARGE PACKAGE"
    else:
        return "UNMAILABLE"
    
print(solve(l, h, t))