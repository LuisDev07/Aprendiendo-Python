def fibonacci(num):
    saquence = []
    a = 0
    b = 1
    for _ in range(num):
        saquence.append(a)
        a, b = b, a + b
    return saquence

fibonacciNum= fibonacci(10)
for numf in fibonacciNum:
    print(numf)
