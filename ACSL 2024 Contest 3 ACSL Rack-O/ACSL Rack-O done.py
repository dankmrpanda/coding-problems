#!/bin/python3

import math
import os
import random
import re
import sys
import copy


#
# Complete the 'playRackO' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING info
#  2. STRING rack
#  3. STRING pile
#
def stepdown(scards):
    steps = 0
    for i in range(1, len(scards)):
        if scards[i] < scards[i-1]:
            steps += 1
    return steps

#assume draw is the next draw card, not the pile list
def ideal_slot(scards, draw, slots, mode): #true if testing, false if impletement
    for i in range(len(slots)):
        if slots[i][0] <= draw <= slots[i][1]:
            if not (slots[i][0] <= scards[i] <= slots[i][1]):
                test = copy.deepcopy(scards)
                test[i] = draw
                if mode:
                    return stepdown(test)
                else:
                    return test
    return None

def ascending(scards, draw, mode):
    for i in range(len(scards) - 2):
        if not (scards[i] < scards[i+1] < scards[i+2]):
            t = False
            test = copy.deepcopy(scards)
            if (draw < scards[i+1] < scards[i+2]):
                test[i] = draw
                t = True
            elif (scards[i] < draw < scards[i+2]):
                test[i+1] = draw
                t = True
            elif (scards[i] < scards[i+1] < draw):
                test[i+2] = draw
                t = True
            if mode and t:
                return stepdown(test)
            elif t:
                return test
    return None
    
def playRackO(info, rack, pile):
    info = info.split()
    s = int(info[0])
    n = int(info[1])
    rack = rack.split()
    pile = pile.split()
    scards = [int(x) for x in rack]
    draw_pile = [int(x) for x in pile]
    
    #region <Defining intervals>
    interval_size = n // s

    if n % s != 0:
        interval_size += 1
    slots = []
    for i in range(s - 1):
        slots.append((i*interval_size + 1, (i+1)*interval_size))
        if i == s - 2:
            slots.append((1 + (i+1)*interval_size, n))
    #endregion
    
    for draw in draw_pile: #holy this is a logic brainfart
        c = stepdown(scards)
        a = ideal_slot(scards, draw, slots, True)
        b = ascending(scards, draw, True)
        # if draw == 71:
        #     breakpoint()
        #     continue
        if (ideal_slot(scards, draw, slots, True) == None and ascending(scards, draw, True) == None):
            continue
        elif (ideal_slot(scards, draw, slots, True) == None):
            if ascending(scards, draw, True) != None:
                if c >= b:
                    scards = ascending(scards, draw, False)
        elif (ascending(scards, draw, True) == None):
            if ideal_slot(scards, draw, slots, True) != None:
                if c >= a:
                    scards = ideal_slot(scards, draw, slots, False)
                
        elif ideal_slot(scards, draw, slots, True) <= ascending(scards, draw, True):
            if c >= a:
                scards = ideal_slot(scards, draw, slots, False)
        else:
            if c >= b:
                scards = ascending(scards, draw, False)
        if stepdown(scards) == 0:
            break
    strings = ""
    for i in scards:
        strings += str(i) + " "
    return strings
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    info = input()

    rack = input()

    pile = input()

    result = playRackO(info, rack, pile)

    fptr.write(result + '\n')

    fptr.close()
