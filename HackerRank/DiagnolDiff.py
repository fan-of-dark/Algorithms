'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
'''

def diagonalDifference(arr):
    n = len(arr)
    i = j = 0
    d1 = d2 = 0
    while i < n and j < len(arr[0]):
        d1+= arr[i][j]
        i+= 1
        j+= 1
    i = 0
    j = len(arr[0]) -1    
    while i < n and j >= 0:
        d2 += arr[i][j]
        i += 1
        j -= 1
    return abs(d1-d2)
