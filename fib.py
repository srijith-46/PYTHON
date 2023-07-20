import time
def timeit(func):
  def timed(*args,**kw):
    ts = time.time()
    print("Start time:",ts)
    execResult = func(*args,**kw)
    te = time.time()
    print("End time:",te)
    print("Total time taken:",te-ts)
    return execResult
  return timed

n = int(input("Enter the length for fibonacii series:"))
@timeit

def fibonacci(n):
  a,b = 0,1
  while True:
    yield a
    a,b = b,a+b
fib=fibonacci(n)
for i in range(n):
  print(next(fib))
