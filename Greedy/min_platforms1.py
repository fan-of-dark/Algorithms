def minimumPlatform(n,arr,dep):
      temp = [0]*(2400)
      maxplat = 0
      for i in range(n):
          temp[int(arr[i])] += 1
          temp[int(dep[i]) + 1] -= 1

      #PREFIX SUMS TO FIND MAX TRAINS AT A POINT OF TIME
      for i in range(1,2400):
          temp[i] += temp[i-1]
          maxplat = max(maxplat,temp[i])
      return maxplat 
