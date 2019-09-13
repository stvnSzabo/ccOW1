n = int(input('N? '))

def Fibonacci(n):
    f0, f1 = 0, 1
    for i in range(n):
        yield f0
        f0, f1 = f1, f0+f1

fibs = list(Fibonacci(n))
fib_sum = sum(fibs)
print(fib_sum)    
