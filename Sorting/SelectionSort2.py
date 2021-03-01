class Solution:
    def selectionSort(self, Arr):
        if len(Arr) == 1:
            return Arr
        else:
            for i in range(len(Arr)-1):
                minm = Arr[i]
                for j in range(i+1,len(Arr)):
                    if Arr[j] < Arr[i]:
                        Arr[i],Arr[j] = Arr[j],Arr[i]
            return Arr            
    
  
