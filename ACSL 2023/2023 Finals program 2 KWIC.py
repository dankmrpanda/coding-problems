#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findARow' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING original
#  2. STRING unused
#  3. STRING rows
#

def findARow(original, unused, rows):
    unused = unused.split()
    original = original.split()
    rows = rows.split()
    og = []
    for i in range(len(original)):
        if original[i][-1] == "." or original[i][-1] == "?" or original[i][-1] == "!" or original[i][-1] == "," or original[i][-1] == ";" or original[i][-1] == ":":
            og.append(original[i][:-1])
            og.append(".")
        else:
            og.append(original[i])
    o = og.copy()
    o = [x.lower() for x in o]

    for i in unused:
        for x in range(len(og)):
            # print(i)
            if o[x] == i:
                o[x] = "."
                og[x] = "."

    words = []
    before = []
    after = []
    # print(og)
    for i in range(len(og)):
        if og[i] == ".":
            continue
        words.append(og[i])

        try:
            b1 = []
            num = 1
            while len(b1) < 3:
                if og[i-num] != ".":
                    b1.insert(0,og[i-num])
                    num = num + 1
                else:
                    raise IndexError
        except IndexError:
            pass
        be = " ".join(b1)
        before.append(be)

        try:
            a1 = []
            num = 1
            while len(a1) < 3:
                if og[i+num] != ".":
                    a1.append(og[i+num])
                    num = num + 1
                else:
                    raise IndexError
        except IndexError:
            pass
        ae = " ".join(a1)
        after.append(ae)

    # for i in range(len(words)):
    #     print(before[i] + ":" + words[i] + ":" + after[i])

    # print(words)
    # print(after)
    word = words.copy()
    word = [x.lower() for x in word]
    # print(word)
    # print(words)
    # print(before)
    for i in range(0,len(words)):
        for j in range(0,len(words)):
            if word[j] > word[i]:
                temp = word[i]
                word[i] = word[j]
                word[j]=temp
                temp = words[i]
                words[i] = words[j]
                words[j]=temp


                temps = after[i]
                after[i] = after[j]
                after[j]=temps

                tempa = before[i]
                before[i] = before[j]
                before[j]=tempa

                # words[i],words[j] = words[j],words[i]
                # after[i],after[j] = after[j],after[i]
                # before[i],before[j] = before[j],before[i]
    # print(after)
    # # print(before)
    # print(word)
    # print(words)
    # for i in range(len(words)):
    #     print(before[i] + ":" + words[i] + ":" + after[i])



    for i in range(len(words)):
        words[i] = words[i][::-1].zfill(len(max(words, key=len)))[::-1]
        before[i] = before[i].zfill(len(max(before, key=len)))
        after[i] = after[i][::-1].zfill(len(max(after, key=len)))[::-1]
        words[i] = words[i].replace("0", "-")
        after[i] = after[i].replace("0", "-")
        before[i] = before[i].replace("0", "-")

    # print(before)
    # print(after)
    mi = int(rows[0])
    minn = words[int(rows[0])].count("-") + after[int(rows[0])].count("-") + before[int(rows[0])].count("-")
    for i in range(int(rows[0])-1, int(rows[1])):
        temp = words[i].count("-") + after[i].count("-") + before[i].count("-")
        # print(words[i] + ":" + str(temp))
        if temp < minn:
            # print(words[i] + ":" + words[mi])
            minn = temp
            mi = i
    return before[mi] + " <" + words[mi] + "> " + after[mi]
    
        
# if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    original = input()

    unused = input()

    rows = input()

    result = findARow(original, unused, rows)

    fptr.write(result + '\n')

    fptr.close()

print(findARow("KWIC is an acronym for Key Word In Context, the most common format for concordance lines which is used for indexing in context.", "for in the", "7 15") == "concordance lines which <is---------> used----------")
print(findARow())