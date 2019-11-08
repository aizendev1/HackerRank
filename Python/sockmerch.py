#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    i = 0
    ar.sort()
    ar.append('*')
    x = 0
    while x < n:
        if ar[x]==ar[x+1]:
            i = i + 1
            x+=2
        else:
            x+=1
    print(i)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

   #fptr.close()

