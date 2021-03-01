def BinaryWithLoops(A,l,u,key):
    while l <= u:
        mid = (l+u)// 2
        if A[mid] == key:
            print(mid)
            break
        elif A[mid] < key:
            l = mid+1
        else:
            u = mid-1
    else:
        print(-1)
