#!/bin/python3

#Day 0: Mean, Median, and Mode

def calculate_Mean_Median_Mode(n,arr):
    sortedArr = sorted(arr)
    d = {}
    #Calculate mean
    getSum = sum(sortedArr)
    mean = getSum/n
    #Calculate median
    if n % 2 == 0:
        nby2_elem = sortedArr[n//2 -1]
        nby2plus1_elem = sortedArr[n//2]
        median = (nby2_elem + nby2plus1_elem)/2
    else:
        median = sortedArr[n//2]
    #Calculate Mode
    for i in sortedArr:
        d[i] = d.get(i,0)+1
    sortedDict = sorted(d.items(), key=lambda item:item[1],reverse=True)
    mode = sortedDict[0][0]
    return mean,median,mode

if __name__ == '__main__':  
    n = int(input())
    arr = [int(i) for i in input().split()]

    mean,median,mode = calculate_Mean_Median_Mode(n,arr)
    print('%.1f'%mean)
    print('%.1f'%median)
    print(mode)