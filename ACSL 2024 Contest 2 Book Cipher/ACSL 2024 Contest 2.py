import re
text = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.  Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.  We are met on a great battle-field of that war.  We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live.  It is altogether fitting and proper that we should do this.  This was written by Abraham Lincoln on 11/19/1863!"

message = "The #1 speech of all time was less than 8 minutes long!"

book = re.split(r'\!  |\?  |\.\  ', text)
book = [re.split(r'[^a-zA-Z0-9]+', s) for s in book]
print(book)
def find_occ(text, letter, n):
    current_occ = 0
    for sentence in range(len(book)):
        for word in range(len(book[sentence])):
            for l in range(len(book[sentence][word])):
                let = book[sentence][word][l]
                if let == letter:
                    current_occ += 1
                    if current_occ == n:
                        return str(sentence + 1) + "." + str(word + 1) + "." + str(l + 1)
    return find_occ(text, letter, max(1, n // 2))

encode = ""
char = 0
sym = True
for i in range(len(message)):
    if message[i] == " ":
        encode += "_"
        sym = True
    elif re.match(r'^[^a-zA-Z0-9]+$', message[i]):
        encode += message[i]
        sym = True
    else:
        if not sym:
            encode += " "
        encode += find_occ(text, message[i], char + 1)
        char += 1
        sym = False
        
print(encode)