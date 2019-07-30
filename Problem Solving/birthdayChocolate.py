#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):#d:sum, s array, m quantity
    summ=0;
    combinations=0;
    for i in range(len(s)):
        if (i+(m-1))<=len(s)-1:
            for j in range(i,i+m):
                summ+=s[j];
            if summ==d:combinations+=1;
        summ=0;
    return combinations;




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
