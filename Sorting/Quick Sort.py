def Partition(A):
    j = 0
    i = -1
    while j < len(A):
        if A[j] > A[-1]:
            j += 1
        else:
            i += 1
            A[i],A[j] = A[j], A[i]
            j +=  1
    return i #pivot position  
  
def quick_sort(A):
    if len(A) == 0 or len(A) == 1:
        return A
    pos = Partition(A)
    return  quick_sort(A[:pos]) + [A[pos]] + quick_sort(A[pos+1:])
