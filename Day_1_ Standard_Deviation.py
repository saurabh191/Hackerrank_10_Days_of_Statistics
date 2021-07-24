#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cal_mean(arr):
    mean = sum(arr)/len(arr)
    return mean

def stdDev(arr):
    mean = round(cal_mean(arr),1)
    num = []
    for i in range(len(arr)):
        num.append((arr[i] - mean)**2)
    stDev = math.sqrt(sum(num)/len(arr))
    
    return round(stDev,1)
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(vals))
