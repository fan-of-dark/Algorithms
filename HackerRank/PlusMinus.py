'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''
'''
Learnt: precision Handling
3 methods:
1.direct -- > print("%.6f" % num)
2..format --> print("{0:.6f}".format(num))
3.round -- > print(round(num,6))
'''
def plusMinus(arr):
    n = len(arr)
    plus = sum([i>0 for i in arr]) /n
    minus = sum([i<0 for i in arr])/n
    zero = sum([i==0 for i in arr])/n
    print("%.6f"%plus)
    print("%.6f"% minus)
    print("%.6f"% zero)
