def minimumPlatform(n,arr,dep):
      arr.sort()
      dep.sort()
      platforms = 1
      maxplatforms = 1

      #2 pointer approach
      i = 1
      j = 0

      #traverse till both exuast
      while i<n and j<n:

          #if train is arraiving before prev trains leave
          if arr[i] <= dep[j]:
              #just add one more platform
              platforms += 1
              #go to next train
              i += 1
          #else empty the platforms after departing prev trains  
          elif arr[i] > dep[j]:
              platforms -= 1
              j += 1
          #at any point, keep the max platforms which are suffecient    
          maxplatforms = max(maxplatforms,platforms)    
      return maxplatforms
