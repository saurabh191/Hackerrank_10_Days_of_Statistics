#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

#Calculate median
def median(arr):
    n = len(arr)
    if n % 2 == 0:
        nby2_elem = arr[n//2 -1]
        nby2plus1_elem = arr[n//2]
        median = (nby2_elem + nby2plus1_elem)//2
    else:
        median = arr[n//2]
    return median   

def quartiles(arr):
    sortedArr = sorted(arr)
    q2 = median(sortedArr)
    q1 = median(sortedArr[0:len(sortedArr)//2])
    q3 = median(sortedArr[(len(sortedArr)//2)+1:])
    return q1,q2,q3


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)
    print(res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
