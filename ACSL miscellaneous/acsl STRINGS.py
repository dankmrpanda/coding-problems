data = "MC-352L/MC-452R/JRDIVISION"
data = data.split("/")
word = data[-1]
data.pop(-1)

def ls(word, shift):
    return word[shift:].ljust(len(word), "#")

def rs(word, shift):
    return word[:-shift].rjust(len(word), "#")

def lc(word, shift):
    return word[shift:] + word[:shift]

def lcmc(word, s, l, x):
    # words = word[s-1:s+l-1]
    # result = word[:s-1] + lc(words, x) + word[s+l:]
    # return result
    return word[:s-1] + lc(word[s-1:s+l-1], x) + word[s+l-1:]

def rc(word, shift):
    return word[len(word) - shift:] + word[:len(word) - shift]

def rcmc(word, s, l, x):
    # words = word[s-1:s+l-1]
    # result = word[:s-1] + rc(words, x) + word[s+l:]
    # return result
    return word[:s-1] + rc(word[s-1:s+l-1], x) + word[s+l-1:]

def mc(word, s, l, x, d):
    if d == "L":
        return lcmc(word, s, l, x)
    else:
        return rcmc(word, s, l, x)

for i in range(len(data)):
    if data[i][:2] == "LS":
        word = ls(word, int(data[i][3:]))
    elif data[i][:2] == "RS":
        word = rs(word, int(data[i][3:]))
    elif data[i][:2] == "LC":
        word = lc(word, int(data[i][3:]))
    elif data[i][:2] == "RC":
        word = rc(word, int(data[i][3:]))
    else:
        print(word)
        word = mc(word, int(data[i][3]), int(data[i][4]), int(data[i][5]), data[i][6])
print(word)