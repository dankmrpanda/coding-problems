#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'encodeMessage' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING text
#  2. STRING message
#
def find_occ(text, letter, n, book):
    current_occ = 0
    for sentence in range(len(book)):
        for word in range(len(book[sentence])):
            for l in range(len(book[sentence][word])):
                let = book[sentence][word][l]
            # for i, c in enumerate(text):
                if let == letter:
                    current_occ += 1
                    if current_occ == n:
                        return str(sentence + 1) + "." + str(word + 1) + "." + str(l + 1)
    return find_occ(text, letter, max(1, n // 2), book)

def encodeMessage(text, message):
    book = re.split(r'\!  |\?  |\.\  ', text)
    book = [re.split(r'[^a-zA-Z0-9]+', s) for s in book]
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
            encode += find_occ(text, message[i], char + 1, book)
            char += 1
            sym = False
    return encode