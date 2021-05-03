N = int(input())
lst = list(map(int,input().split()))
jobs = []
maxdeadline = 0
for i in range(0,len(lst)-2,3):
    jobs.append((lst[i+2],lst[i+1],lst[i]))
    maxdeadline = max(maxdeadline,lst[i+1])
arr = [-1]*(maxdeadline+1)
jobs.sort(reverse= True)
res = 0
for job in jobs:
    if -1 not in arr[1:]: break
    j = job[1]
    while j >= 1:
        if arr[j] == -1:
            arr[j] = job[2]
            res += job[0]
            break
        j -= 1  
print(res)            
