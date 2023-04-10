#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    for x in range(len(arr)):
        if arr[x] > 0:
            plus += 1
        elif arr[x] < 0:
            minus += 1
        elif arr[x] == 0:
            zero += 1
    plus = plus / (len(arr))
    minus = minus / (len(arr))
    zero = zero / (len(arr))
    print(f'{plus:.6f}')
    print(f'{minus:.6f}')
    print(f'{zero:.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
