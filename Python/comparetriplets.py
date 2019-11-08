#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    i = 0
    while i <= len(a) and len(a) <= 3 and len(b) <= 3:
        if a[0] > b[0]:
            alice += 1
        elif b[0] > a[0]:
            bob += 1
        if a[1] > b[1]:
            alice += 1
        elif b[1] > a[1]:
            bob += 1
        if a[2] > b[2]:
            alice += 1
        elif b[2] > a[2]:
            bob += 1
        print(alice, bob)
        break
if __name__ == '__main__':
    #fptr = open("test.txt", 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

