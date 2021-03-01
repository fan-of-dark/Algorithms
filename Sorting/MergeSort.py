def merge(A,B):
    C = []
    i = j = k= 0
    while i< len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
        k+= 1
    if i != len(A):
        C.extend(A[i:])
    if j != len(B):
        C.extend(B[j:])
    return C
  
  def merge_sort(A):
    #base case
    if len(A) == 1 or len(A) == 0:
        return A
    else:
        mid = len(A)//2 
        l = merge_sort(A[:mid])
        r = merge_sort(A[mid:])
        return merge(l,r) 
