import re
text = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.  Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure.  We are met on a great battle-field of that war.  We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live.  It is altogether fitting and proper that we should do this.  This was written by Abraham Lincoln on 11/19/1863!"

message = "The #1 speech of all time was less than 8 minutes long!"

book = re.split(r'\!  |\?  |\.\  ', text) #split text into array of sentences based on !, ?, .
book = [re.split(r'[^a-zA-Z0-9]+', s) for s in book] #split each sentence into array of words based on all symbols
print(book)

def find_occ(text, letter, n): #finds the s.w.c value based on text, letter, and occurrence #
    current_occ = 0 #used to check if occurrence matches specficed one
    for sentence in range(len(book)): #only used len() because s.w.c requires numbers
        for word in range(len(book[sentence])):
            for l in range(len(book[sentence][word])):
                let = book[sentence][word][l] #let is now equal to a singular letter
                if let == letter: #checks if let is equal to the wanted number
                    current_occ += 1 #if so add occurrence # by 1
                    if current_occ == n: #if occurrence # is equal to the wanted number
                        return str(sentence + 1) + "." + str(word + 1) + "." + str(l + 1) #return s.w.c format (add one since index starts at 0)
    return find_occ(text, letter, max(1, n // 2)) #if the current occurrence # is too high, try again recursively with //2

encode = ""
char = 0
sym = True
for i in range(len(message)): #iterate through message
    if message[i] == " ": #checks if its a space, if so, add "_" to encode
        encode += "_"
        sym = True #this is for the spacing issue (when to put a space), probably not the best way to solve but
    elif re.match(r'^[^a-zA-Z0-9]+$', message[i]): #checks if the selected letter is a symbol
        encode += message[i] #if so, add symbol to encode
        sym = True
    else:
        if not sym: #if there wasnt a symbol/space before it, add a space
            encode += " "
        encode += find_occ(text, message[i], char + 1) #append the output of s.w.c to encode
        char += 1 #since symbols do not count as characters, add one only if its a character (non symbols)
        sym = False #reset symbol variable
        
print(encode)