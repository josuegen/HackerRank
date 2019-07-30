#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max=0;
    min=0;
    maxtimes=0;
    mintimes=0;
    max=min=scores[0];
    records=[];
    for i in range(len(scores)):
        if(scores[i]>max):
            maxtimes+=1;
            max=scores[i];
        elif(scores[i]<min):
            mintimes+=1;
            min=scores[i];
    records.append(maxtimes);
    records.append(mintimes);
    return records;


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
