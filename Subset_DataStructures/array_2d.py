#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = -100
    for i in range(1, 5):
        for j in range(1, 5):
            val = get_hourglass(arr, i,j)
            print (val)
            if val > max:
                max = val

    return max

def main():
    test = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2]]

    val = hourglassSum(test)
    print (val)

def get_hourglass(arr,i,j):

    top = arr[i-1][j-1:j+2]
    bottom = arr[i+1][j-1:j+2]
    middle = arr[i][j]

    sum_all = sum(top) + sum(bottom) + middle


    return sum_all

if __name__ == "__main__":
    main()

"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()"""