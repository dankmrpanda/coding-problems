def fibCypher(key, msg):
    alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    ending=""
    a=0
    fibindex=1
    for i in range(len(msg)):
        c = a + fibindex
        a = fibindex
        fibindex = c
        keyindex=alphabet.index(key)
        keyindex=keyindex+fibindex
        keyindex=keyindex%26
        offset=alphabet[keyindex]
        offsets=ord(offset)
        char=ord(msg[i])
        end=char+offsets
        ending=ending+str(end)+" "
    return ending
