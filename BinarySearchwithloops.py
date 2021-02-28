n = int(input())
lst = list(map(int,input().split()))
key = int(input())
#initialiaing the low,high,mid
lst.sort()
low = 0
high = len(lst)
mid = (low+high)//2 

#looping 
while(lst[mid] != key and high >= low):
    mid = (low+high)//2
    
    if lst[mid] == key:
        print(1)
        break
    else:
        if lst[mid] > key:
            high = mid-1
        else:
            low = mid+1
else:
    print(-1)
            



