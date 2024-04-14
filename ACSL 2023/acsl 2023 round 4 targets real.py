'''
PROBLEM STATEMENT:
Given the nx n grid with target locations and with empty border cells, place arrows
in every border cell and find the target(s) that get(s) hit the most. The arrow stops
when it hits a target. The arrows that can be placed in any border cell are defined as
A-H: (A) <-, (B) ↑, (C) →, (D) ↓, (E) ^\, (F) ^/, (G) \v, and (H) /v. Output the 
location(s) of the target(s) as 2-character strings separated by a single space in 
row-column order. The upper left corner is identified as location (0,0) using row-major
order.


EXAMPLE:
In the grid below, the size is 6 x 6 with 5 different targets.

-------------------------
|   |   |   |   |   |   |
|---|---|---|---|---|---|
|   |   |   | X |   |   |
|---|---|---|---|---|---|
|   | X |   |   |   |   |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
|---|---|---|---|---|---|
|   | X | X |   | X |   |
|---|---|---|---|---|---|
|   |   |   |   |   |   |
-------------------------

By checking every border position, the following arrows will hit each target:

----------------------------------------------------------------------------------------------------------
| Target | Border    | Border    | Border    | Border    | Border    | Border    | Border    | Border    |
|        | cell and  | cell and  | cell and  | cell and  | cell and  | cell and  | cell and  | cell and  |
|        | direction | direction | direction | direction | direction | direction | direction | direction |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| (1, 3) | 02G       | 03D       | 04H       | 10C       | 15A       | 35E       | 40F       | 53B       |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| (2, 1) | 01D       | 03H       | 10G       | 20C       | 25A       | 30F       | 54E       |           |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| (4, 1) | 05H       | 30G       | 40C       | 50F       | 51B       | 52E       |           |           |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| (4, 2) | 02D       | 15H       | 20G       | 51F       | 52B       | 53E       |           |           |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| (4, 4) | 00G       | 04D       | 35H       | 45A       | 53F       | 54B       | 55E       |           |
----------------------------------------------------------------------------------------------------------



TASK:
Complete the function targetsWithMostArrows that is called from a program that inputs 
the following data as its parameters and outputs the following information for each 
individual input:

• The function has 2 parameters: a number, size, representing the size of the grid and 
a string, targets, representing the locations of the targets as 2-character strings 
separated by a single space

• The function should return a string of 2-character strings, in row-column order, 
representing the location of the target(s) that could be hit by the most arrows without 
encountering another target

You may create additional functions that are called from targetsWithMostArrows if needed 
in solving the problem.

CONSTRAINTS:
The inputted number will be no more than 10. The locations of the targets will all be on 
the grid and not in any border cells.

DATA PROVIDED:
There are 5 sets of Sample Data for debugging and 5 sets of Test Data for scoring. 
You may create additional data sets for debugging your program.

'''

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'targetsWithMostArrows' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER size
#  2. STRING targets
#

def leftup(r, c, tar, size):
    l = min(r, c)
    for i in range(1, l+1):
        for x in range(len(tar)):
            if(r-i == tar[x][0] and c-i == tar[x][1]):
                return 1
    return 0
            
def rightup(r, c, tar, size):
    l = min(r, (size-1)-c)
    # print("add num: "+str(l))
    for i in range(1, l+1):
        # print("checking: "+str(r-i) + str(c+i))
        for x in range(len(tar)):
            if(r-i == tar[x][0] and c+i == tar[x][1]):
                return 1
    return 0

def leftdown(r, c, tar, size):
    l = min((size-1)-r, c)
    for i in range(1, l+1):
        for x in range(len(tar)):
            if(r+i == tar[x][0] and c-i == tar[x][1]):
                return 1
    return 0
            
def rightdown(r, c, tar, size):
    l = min((size-1)-r, (size-1)-c)
    for i in range(1, l+1):
        for x in range(len(tar)):
            if(r+i == tar[x][0] and c+i == tar[x][1]):
                return 1
    return 0
            

def left(r, c, tar, size):
    for i in range(1, c+1):
        for x in range(len(tar)):
            if(r == tar[x][0] and c-i == tar[x][1]):
                return 1
    return 0

def right(r, c, tar, size):
    l = (size-1)-c
    for i in range(1, l+1):
        for x in range(len(tar)):
            if(r == tar[x][0] and c+i == tar[x][1]):
                return 1
    return 0

def up(r, c, tar, size):
    for i in range(1, r+1):
        for x in range(len(tar)):
            if(r-i == tar[x][0] and c == tar[x][1]):
                return 1
    return 0
            
def down(r, c, tar, size):
    l = (size-1)-r
    for i in range(1, l+1):
        for x in range(len(tar)):
            if(r+i == tar[x][0] and c == tar[x][1]):
                return 1
    return 0

def targetsWithMostArrows(size, targets):
    targets = targets.split()
    tar = []
    for i in range(len(targets)):
        tar.append([*targets[i]])
    for i in range(len(tar)):
        tar[i][0] = int(tar[i][0])
        tar[i][1] = int(tar[i][1])
        
    count = []
    for i in range(len(tar)):
        r = tar[i][0]
        c = tar[i][1]
        # print(leftup(r, c, tar, size))
        # print(rightup(r, c, tar, size))
        # print(leftdown(r, c, tar, size))
        # print(rightdown(r, c, tar, size))
        # print(left(r, c, tar, size))
        # print(right(r, c, tar, size))
        # print(up(r, c, tar, size))
        # print(down(r, c, tar, size))
        # print(str(r) + str(c))
        # print("______________")
        count.append(8-(leftup(r, c, tar, size)+rightup(r, c, tar, size)+leftdown(r, c, tar, size)+rightdown(r, c, tar, size)+left(r, c, tar, size)+right(r, c, tar, size)+up(r, c, tar, size)+down(r, c, tar, size)))
    final = ""
    fin = [i for i, x in enumerate(count) if x == max(count)]
    for i in range(len(fin)):
        final = final + targets[fin[i]]+" "
    finall = final.split()
    finall.sort()
    ff = " ".join(map(str, finall))
    # print(ff)
    return ff