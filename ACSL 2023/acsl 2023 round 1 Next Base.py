'''1. Next Base (2022-2023)

PROBLEM STATEMENT:
Given 3 positive integers, n, b, and s, generate the next n numbers in base b starting with s in the given base.
We guarantee that the base will be between 2 and 9 inclusive. We guarantee that s is a valid number in base b. 
Find the base 10 value for the number of times the largest possible digit in the given base is found among all 
of the digits in the numbers generated.

EXAMPLE:
If n=15, 6-8, and s-2, the numbers generated are 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20. 
The largest possible digit in base 8 is 7 which occurs 2 times.

TASK:
Complete the function countLargest Digit:
• The function has 3 parameters: an integer, num, representing the number of values to be found, an integer, base,
representing the base to be used between 2 and 9 inclusive, and an integer, start, representing the starting value
in the base given
• The function returns a base 10 number representing the number of times the largest possible digit in the given base
is found among all of the digits in the numbers generated

You may create additional functions that are called from countLargest Digit if needed in solving the problem.


CONSTRAINTS:
All inputs will be integer values. The base will be between 2 and 9 inclusive. We guarantee that start is a valid number in the given base.
The starting number will be no more than 16 digits long.
DATA PROVIDED:
There are 5 sets of Sample Data for debugging and 5 sets of Test Data for scoring. You may create additional data sets for debugging your program.
'''

def tobase10(base, data):
    data=[int(d) for d in str(data)]
    p=len(data)-1
    ans=0;
    for i in range(len(data)):
        ans+=data[i]*(pow(base, p))
        p-=1
    return ans

def base10to(base, data):
    ans=''
    summ=data
    while(summ!=0):
      x=summ%base
      summ=summ//base  
      ans=str(x)+ans
    return ans

def countLargestDigit(num, base, start):
    count=0
    starts=tobase10(base, start)
    lst=""
    i=0
    while(count<num):
        lst+=base10to(base, starts+i)
        lst+=","
        count+=1
        i+=1
        print(lst)
    a=lst.count(str(base-1))
    return a

print(countLargestDigit(20, 3, 12))