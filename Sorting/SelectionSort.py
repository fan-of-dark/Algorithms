class Solution:
    def selectionSort(self, Arr):
        for i in range(len(Arr)):
            minm = Arr.index(min(Arr[i+1:]))
            min_index = i 
            for j in range(i+1, len(Arr)): 
                if Arr[min_index] > Arr[j]: 
                    min_index = j
            print(minm)        
            print(min_index)        
            Arr[i], Arr[min_index] = Arr[min_index], Arr[i]
            
            
        return Arr        
    
  
