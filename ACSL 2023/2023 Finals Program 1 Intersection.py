#!/bin/python3

import math
import os
import random
import re
import sys


intervals1 = "(5,10) (-5,2] [24,28] [12,22)"
intervals2 = "[1,4] [15,25) [-4,-1) (7,12]"
intervals3 = "null"


intervals1 = intervals1.replace(" ", ",")
intervals1 = intervals1.split(",")
intervals2 = intervals2.replace(" ", ",")
intervals2 = intervals2.split(",")
if intervals3 != "null":
    null = True
    intervals3 = intervals3.replace(" ", ",")
    intervals3 = intervals3.split(",")

if(not null):
    























#
# Complete the 'sumsNotCommon' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING intervals1
#  2. STRING intervals2
#  3. STRING intervals3
#

# def sumsNotCommon(intervals1, intervals2, intervals3):
    
    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     intervals1 = input()

#     intervals2 = input()

#     intervals3 = input()

#     result = sumsNotCommon(intervals1, intervals2, intervals3)

#     fptr.write(result + '\n')

#     fptr.close()
