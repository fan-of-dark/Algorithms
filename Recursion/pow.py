def myPow(self, x: float, n: int) -> float:
  if n == 0:
      return 1
  elif n < 0:
      return self.myPow(1/x,-n)

  temp = self.myPow(x,n//4)
  res = temp * temp * temp * temp
  if n%4 == 1:
      res *= x
  elif n%4 == 2:
      res *= x*x
  elif n%4 == 3:
      res *= x*x*x
  return res
