

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges,m,n):
    applesFallen=[];
    orangesFallen=[];
    orangesAtHouse=0;
    applesAtHouse=0;
    for j in range (m):
        applesFallen.append(a+apples[j]);
        if(s <= applesFallen[j] <=t ):
            applesAtHouse+=1;
    for k in range (n):
        orangesFallen.append(b+oranges[k]);
        if(s <= orangesFallen[k] <= t):
            orangesAtHouse+=1;
    print(str(applesAtHouse));
    print(str(orangesAtHouse));

    
    
    


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges,m,n)
