def activitySelection(self,n,start,end):
    acts = []
    res = 0
    for i,j in zip(start,end):
        acts.append((i,j))
    acts.sort(key = lambda x:x[1])
    res += 1
    f = acts[0][1]
    for i,j in acts:
        if i > f:
            res += 1
            f = j
    return res
