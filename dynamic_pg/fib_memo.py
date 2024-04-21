# SOlution o(2^n), time error
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return  fib(n - 1) + fib(n - 2)  

# right one
def fib(n):
  return  fib(n, {}) 

def _fib(n, memo):
  if n in memo:
    return memo[n]
  if n == 0:
    return 0
  if n == 1:
    return 1
  memo[n] = _fib(n -1, memo) + _fib(n - 2, memo) 
  return memo[n]  