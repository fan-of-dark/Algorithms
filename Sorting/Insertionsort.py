class Solution:
    def insertionSort(self, Arr):
        n = len(Arr)
        for i in range(1,n):
            j = i
            while (j != 0 and Arr[j] < Arr[j-1]):
                if Arr[j] < Arr[j-1]:
                    Arr[j],Arr[j-1] = Arr[j-1],Arr[j]
                j -= 1
        return Arr        
            
