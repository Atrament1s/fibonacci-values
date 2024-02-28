import math

n = math.floor(int(input("\nHow many Fibonacci numbers would you like to generate?\n")))
init0 = 0
init1 = 0
counter = 0

def fib(x, y):
    if counter == 1 or x+y > 0:
        return x+y
    else:
        return x+y+1

for x in range(n):
    counter += 1
    fibVal = fib(init0, init1)
    init0 = init1
    init1 = fibVal
    if counter == n:
        print(str(fibVal) + "\n")
    elif counter == 1:
        print("\n" + str(fibVal))
    else:
        print(fibVal)
