'''
1. Binary Counting
PROBLEM STATEMENT:
Given a string of characters found on the keyboard, convert each character in the string to the binary 
equivalent of its ASCII code. In the resulting concatenated string, search for the increasing sequence 
of binary numbers starting with 0, 1, 10, 11, ... until a number cannot be found anywhere in the string. 
Look from the start of the string. If the binary number is found, remove that occurrence of the binary 
number from the string. Then look from the end of the string. If the binary number is found, remove 
that occurrence of the binary number from the string. When the binary number cannot be found at all, 
output the decimal equivalent of the last binary number that can be found.

EXAMPLE:
For the string "Roses are red.", convert it to a concatenated string of binary numbers using each 
character's ASCII code as follows:

---------------------------------------------------------
| Char | ASCII |  Binary  |     | Char | ASCII | Binary |
-------------------------------------------------------
| R    | 82    | 01010010 |     | r    | 114 | 01110010 |
-------------------------------------------------------
| o    | 111   | 01101111 |     | e    | 101 | 01100101 |
-------------------------------------------------------
| s    | 115   | 01110011 |     | sp   | 32  | 00100000 |
-------------------------------------------------------
| e    | 101   | 01100101 |     | r    | 114 | 01110010 |
-------------------------------------------------------
| s    | 115   | 01110011 |     | e    | 101 | 01100101 |
-------------------------------------------------------
| sp   | 32    | 00100000 |     | d    | 100 | 01100100 |
-------------------------------------------------------
| a    | 97    | 01100001 |     | .    | 46  | 00101110 |
---------------------------------------------------------

Now search for binary numbers beginning with 0 in the following string:
    (0)1110011 01100101 01110011 00100000 01100001 01110010 
    01100101 00100000 01110010 01100101 01100100 0010111(0)
    
Remove the 0 from both ends so the string becomes:
    (1)010010 01101111 01110011 01100101 01110011 00100000 01100001
    01110010 01100101 00100000 01110010 01100101 01100100 001011(1)

Remove the 1 from both ends so the string becomes:
    0(10)010 01101111 01110011 01100101 01110011 00100000 01100001
    01110010 01100101 00100000 01110010 01100101 01100100 00(10)11

Remove 10 from both ends so the string becomes:
    0010 0(11)01111 01110011 01100101 01110011 00100000 01100001
    01110010 01100101 00100000 01110010 01100101 01100100 00(11)
    
Remove 11 from both ends so the string becomes:
    00(10 0)01111 01110011 01100101 01110011 00100000 01100001 
    01110010 01100101 00100000 01110010 01100101 01100(100) 00
    
Continuing until we search for 1001, the resulting string is:
    00001(1010)101110011000001100001011100100110010000000001000100
    
The string 1010 can only be found once from the start of the string so the resulting string is:
    00001101110011000001100001011100100110010000000001000100
    
The process continues until the final string becomes:
    0000110000011000010010010000000001000100
    

TASK:
• Complete the function findLastBinary that is called from a program that inputs the following data as 
  its parameters and outputs the following information for each individual input:
• The function has one parameter: a string, s, that will be converted to binary using each character's 
  ASCII code
• The function should return an integer representing the decimal equivalent to the last binary number 
  that can be found in the string after all deletions have been made
  
You may create additional functions that are called from findLastBinary if needed in solving the problem.


CONSTRAINTS:
The input string may contain any character on the keyboard. The string will be fewer than 200 characters.

DATA PROVIDED:
There are 5 sets of Sample Data for debugging and 5 sets of Test Data for scoring. You may create additional 
data sets for debugging your program.


DATA:
    
-------------------------------------------------------------------------
| CASE | INPUT                                        | EXPECTED OUTPUT |
-------------------------------------------------------------------------
| 0    | "Roses are red."                             | 12              |
-------------------------------------------------------------------------
| 1    | "A is Alpha; B is Bravo; C is Charlie."      | 20              |
-------------------------------------------------------------------------
| 2    | "A stitch in time saves nine."               | 14              |
-------------------------------------------------------------------------
| 3    | "1, 2: Buckle my shoe! 3, 4: Shut the door!" | 22              |
-------------------------------------------------------------------------
| 4    | "Is HackerRank the platform used by ACSL?"   | 27              |
-------------------------------------------------------------------------
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findLastBinary' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def findLastBinary(s):
    data=[*s]
    bi=""
    for i in range(len(data)):
        ascii=ord(data[i])
        bina=bin(ascii)
        bina=bina[2:]
        bi+= bina.zfill(8)
    # bi=bi[:-1]
    # bi=bi.replace(" ", "")
    cts=0
    # print(bi)
    # print("\n")
    while True:
        count=bin(cts)[2:]
        # print(count)
        index=bi.find(count)
        
        if index != -1:
            bi = bi[:index] + bi[index+len(count):]
            
        rindex=bi.rfind(count)
        if rindex != -1:
            bi = bi[:rindex] + bi[rindex+len(count):]
        
        if index==-1 and rindex==-1:
            # print(index)
            # print(rindex)
            # print(count)
            break
        # print(bi)
        # print(index)
        # print(rindex)
        # print("\n")
        cts+=1
    return cts-1


