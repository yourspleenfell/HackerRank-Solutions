#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for x in range(n):
        space = int(n - (x) - 1)
        pound = x + 1
        print(f'{" "*space}{"#"*pound}')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
