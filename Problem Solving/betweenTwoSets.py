#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    candidates=[];
    candidates2=[];
    r=[];
    factors=0;
    multipliers=0;
    for i in range(len(b)):
        for j in range(b[i]+1):
            if(j!=0):#and j!=1
                if(b[i]%j==0):
                    if j not in candidates: candidates.append(j);
    for i in range(len(candidates)):
        for j in range(len(b)):
            if(b[j]%candidates[i]==0):
                multipliers+=1;
        if(multipliers==len(b)):candidates2.append(candidates[i]);
        multipliers=0;
    candidates=[];
    for i in range(len(candidates2)):
        for j in range(len(a)):
            if(candidates2[i]%a[j]==0):
                factors+=1;
        if factors==len(a) and candidates2[i] not in r: r.append(candidates2[i]);
        factors=0;
    return len(r);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
