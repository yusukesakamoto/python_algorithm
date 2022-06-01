def multiple_total(a, b):
  ans = 0
  num = 1
  while True:
   if num * a > b:break
   ans += num * a
   num += 1
    
  return ans