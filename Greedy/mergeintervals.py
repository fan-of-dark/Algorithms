def merge(self, intervals: List[List[int]]) -> List[List[int]]:
  intervals.sort()
  res = []
  s = intervals[0][0]
  f = intervals[0][1]
  for i in intervals[1:]:
      if i[0] <= f:
          f = max(i[1],f)
      else:
          res.append([s,f])
          s = i[0]
          f = i[1]
  res.append([s,f])        
  return res
