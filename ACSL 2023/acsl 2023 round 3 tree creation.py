'''
1. Tree Creation
PROBLEM STATEMENT:
Given a string to create 2 parallel arrays, process the letters in the string from left 
to right, inserting each letter into the first array in alphabetical order, one letter 
at a time. During this process, each letter is assigned an integer value in the second 
array as follows:

1. The first letter has a value of 0.
2. If the new letter is the first or last in the array, its value is one more than the 
value of the adjacent letter.
3. Otherwise, it is one more than the larger value of the two adjacent values. If the 
letter is already in the array, the new letter is placed before the existing letter.


Once the two arrays are created, print two different strings separated by a single space. 
For each letter in the array from left to right:
    
• Check if there is a letter to the left of it that has a value that is one greater than 
its value. Stop if you encounter any value that is less than its value. If a letter meets 
the condition above, add it to the first string.

• Check if there is a letter to the right of it that has a value that is one greater than 
its value. Stop if you encounter any value that is less than its value. If a letter meets 
the condition above, add it to the second string.

• Do not add the letter if it would be in both strings.

If either string is empty, print NONE instead.

EXAMPLE #1:
Test instructions
Here is how the array is built for the string PYTHONN:
The letter P illustrates rule 1; Y and H illustrate rule 2; the T, O and both Ns 
illustrate rule 3; and the final N illustrates what happens if there is a duplicate letter.

-------------------------------------------
| P | Letters | P |   |   |   |   |   |   |
|   |--------------------------------------
|   | Values  | 0 |   |   |   |   |   |   |
-------------------------------------------
| Y | Letters | P | Y |   |   |   |   |   |
|   |--------------------------------------
|   | Values  | 0 | 1 |   |   |   |   |   |
-------------------------------------------
| T | Letters | P | T | Y |   |   |   |   |
|   |--------------------------------------
|   | Values  | 0 | 2 | 1 |   |   |   |   |
-------------------------------------------
| H | Letters | H | P | T | Y |   |   |   |
|   |--------------------------------------
|   | Values  | 1 | 0 | 2 | 1 |   |   |   |
-------------------------------------------
| O | Letters | H | O | P | T | Y |   |   |
|   |--------------------------------------
|   | Values  | 1 | 2 | 0 | 2 | 1 |   |   |
-------------------------------------------
| N | Letters | H | N | O | P | T | Y |   |
|   |--------------------------------------
|   | Values  | 1 | 3 | 2 | 0 | 2 | 1 |   |
-------------------------------------------
| N | Letters | H | N | N | O | P | T | Y |
|   |--------------------------------------
|   | Values  | 1 | 4 | 3 | 2 | 0 | 2 | 1 |
-------------------------------------------

In these final arrays, process each letter as follows:
    
• The letter H has a value of 1. Searching to its left, no letter is found. Searching to 
its right, a value of 2 is found. Add H to the second string.

• The 1st N has a value of 4. Searching to its left, there is no 5. Searching to its right, 
no 5 is found before encountering the 3. It is not added to either string.

•The 2nd N has a value of 3. Searching to its left, there is a 4. Searching to its right, 
there is no 4 before encountering the 2. Add N to the first string.

• The O has a value of 2. Searching to its left, there is a 3. Searching to its right, there 
is no 3 before encountering the 0. Add O to the first string.

• The P has a value of 0. Searching to its left, there is a 1. Searching to its right, there 
is a 1. Do not add it to either string.

• The T has a value of 2. Searching to its left, there is no 3 before encountering the 0. 
Searching to its right, there is no 3. It is not added to either string.

• The Y has a value of 1. Searching to its left, there is a 2. Searching to its right, no 
letter is found. It is added to the first string. The output is NOY H.


EXAMPLE #2:
The string BINARYSEARCHTREE results in the following array:

---------------------------------------------------------------------------
| Letters | A | A | B | C | E | E | E | H | I | N | R | R | R | S | T | Y |
---------------------------------------------------------------------------
| Values  | 2 | 1 | 0 | 3 | 5 | 4 | 2 | 3 | 1 | 2 | 5 | 4 | 3 | 5 | 6 | 4 |
---------------------------------------------------------------------------

Following the same process as above, the output is AERY CNS.


TASK:
Complete the function onlyLeftOrRight that is called from a program that inputs the following 
data as its parameters and outputs the following information for each individual input:
• The function has 1 parameter: a string, input, representing the string to use in building the 
two arrays

• The function should return a concatenated string of the first string and the second string 
separated by a single space

You may create additional functions that are called from onlyLeftOrRight if needed in solving 
the problem.

CONSTRAINTS:
The inputted string will be no more than 80 characters containing all capital letters.

DATA PROVIDED:
There are 5 sets of Sample Data for debugging and 5 sets of Test Data for scoring. You may create 
additional data sets for debugging your program.
''' 


#
# Complete the 'onlyLeftOrRight' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING input as parameter.
#

def onlyLeftOrRight(input):
    input = [*input]
    a1 = [input[0]]
    a2 = [0]
    input.pop(0)
    count = 0
    for i in range(len(input)):
        if input[i] in a1:
            temp = a1.index(input[i])
            a1.insert(temp, input[i])
            if temp == 0:
                count = a2[0] + 1
            else:
                count = max(a2[temp-1], a2[temp]) + 1
            a2.insert(temp, count)
        else:
            for x in range(len(a1)):
                if input[i] < a1[x]:
                    a1.insert(x, input[i])
                    if x == 0:
                        count = a2[0] + 1
                    else:
                        count = max(a2[x-1], a2[x]) + 1
                    a2.insert(x, count)
                    break
            else:
                a1.append(input[i])
                count = a2[-1] + 1
                a2.append(count)
                
    s1 = ""
    s2 = ""
    check1 = False
    check2 = False
    
    for i in range(len(a1)):
        for x in range(i-1, -1, -1):
            if a2[i] > a2[x]:
                break
            elif a2[i] + 1 == a2[x]:
                check1 = True
                break
        
        for x in range(i+1, len(a2)):
            if a2[i] > a2[x]:
                break
            elif a2[i] + 1 == a2[x]:
                check2 = True
                break
        if check1 == True and check2 == False:
            s1 += a1[i]
        elif check1 == False and check2 == True:
            s2 += a1[i]
        # print("s1: " +s1)
        # print("s2: " +s2)
        check1 = False
        check2 = False
    
    if len(s1) == 0:
        s1 = "NONE"
    if len(s2) == 0:
        s2 = "NONE"
    return s1 + " " + s2


print(onlyLeftOrRight("PYTHONN") == "NOY H")
print(onlyLeftOrRight("BINARYSEARCHTREE") == "AERY CNS")
print(onlyLeftOrRight("CORONAVIRUS") == "NOUV NONE")
print(onlyLeftOrRight("FINALSFORACSL") == "FLS IOR")
print(onlyLeftOrRight("HACKERRANKPLATFORM") == "AR CEL")
#holy fuck i suck at coding