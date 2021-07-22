#!/bin/python3

#Day 0: Weighted Mean

import math
import os
import random
import re
import sys


def calculate_weightedMean(X, W):
    productArr = []
    for i in range(len(X)):
        productArr.append(X[i]*W[i])
    weighted_Mean = sum(productArr)/sum(W)

    return round(weighted_Mean,1)


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean = calculate_weightedMean(vals, weights)
    print(weightedMean)
