#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    for x in range(len(arr)):
        temp_arr = arr.copy()
        temp_arr.pop(x)
        temp_sum = sum(temp_arr)
        if max_sum < temp_sum:
            max_sum = temp_sum
        if min_sum == 0 or min_sum > temp_sum:
            min_sum = temp_sum
    print(f'{min_sum} {max_sum}')           


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
