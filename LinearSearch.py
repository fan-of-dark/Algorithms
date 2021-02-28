n = int(input())
lst = list(map(int,input().split()))
key = int(input())
for i in range(len(lst)-1,-1,-1):
    if lst[i] == key:
        print(i)
        break
else: print("No")
