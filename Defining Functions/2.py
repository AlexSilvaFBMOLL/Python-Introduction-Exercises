def factorial(n):
  fact = 1
  for x in range(1,n+1):
    fact *= x
  return fact

def factorialRecursivo(n):
  if n<=1:
    return 1
  else:
    return n * factorialRecursivo(n-1)

print(factorial(1558))