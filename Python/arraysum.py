#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    answer=0;
    for i in range(len(ar)):
        answer+=ar[i]
    print(answer)

if __name__ == '__main__':

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

