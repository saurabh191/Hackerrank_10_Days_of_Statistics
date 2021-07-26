#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
    n = len(arr)
    if n % 2 == 0:
        nby2_elem = arr[n//2 -1]
        nby2plus1_elem = arr[n//2]
        # print(nby2_elem)
        # print(nby2plus1_elem)
        median = (nby2_elem + nby2plus1_elem)//2
    else:
        median = arr[n//2]
    return median   

def quartiles(arr):
    sortedArr = sorted(arr)
    q2 = median(sortedArr)
    # print(sortedArr)
    # print(sortedArr[:len(sortedArr)//2])
    q1 = median(sortedArr[0:len(sortedArr)//2])
    # print("q1",q1)
    if len(sortedArr)%2 != 0:
        # print(sortedArr[(len(sortedArr)//2)+1:])
        q3 = median(sortedArr[(len(sortedArr)//2)+1:])
        # print("q3",q3)
    else:
        # print(sortedArr[(len(sortedArr)//2):])
        q3 = median(sortedArr[(len(sortedArr)//2):])
        # print("q3",q3)
    return q1,q3

def interQuartile(values, freqs):
    data = []

    for i in range(len(values)):
        for j in range(freq[i]):
            data.append(values[i])
    # print(sorted(data))
    q1,q3 = quartiles(data)
    iqr = q3 -q1
    print('%.1f'%iqr)
    
    return


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
