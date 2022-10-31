# for nth term in fibonacci sequence:

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#print(fib(20))

# for fibonacci sequence up until nth term:

def fib_full(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return(fib(x-1)+fib(x-2))

x = 100

for i in range(0,x):
    print(fib(i), end=" ")
