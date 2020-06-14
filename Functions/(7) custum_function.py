def fibonacci(n):
  a = 0
  b = 1
  result = []
  while a < n:
    result = result + [a]
    # result.append(a)
    a, b = b, a + b
  
  return result


print(fibonacci(200))