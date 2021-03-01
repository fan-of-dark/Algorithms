'''
using loop-1
def gcd(n1,n2):
    if (n1 > n2): i = n2
    else: i = n1
    while i >= 0:
        if n1%i ==0 and n2%i == 0:
            gcd = i
            break
        i -= 1    
    return gcd
'''

def gcdr(a,b):
    if a == b:
        return a
    if a > b:return gcdr(a-b,b)
    else: return gcdr(a,b-a) 
