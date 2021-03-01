def Binary(A,l,u,key):
    if len(A) == 0 :
        return -1
    mid = (l+u)//2
    if A[mid] == key:
        return mid
    elif A[mid] > key:
        u = mid -1 
    else:
        l = mid +1 
    return Binary(A,l,u,key)   
