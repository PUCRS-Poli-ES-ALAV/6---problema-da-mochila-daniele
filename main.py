#FIBO-REC (n)
#   se n ≤ 1
#   então devolva n
#   senão a ← FIBO-REC (n − 1)
#         b ← FIBO-REC (n − 2)
#         devolva a + b

def fib_rec(n):
    if(n <= 1):
        return n
    else:
        a = fib_rec(n-1)
        b = fib_rec(n-2)
        return a + b

print(f"Fibonacci recursivo: {fib_rec(5)}")

#FIBO (n)
#     f [0] ← 0 
# f [1] ← 1
# para i ← 2 até n faça
#        f[i] ← f[i-1]+f[i-2]
# devolva f [n]

fib_array = list()

def fib(n):
    fib_array.insert(0, 0)
    fib_array.insert(1, 1)

    for i in range(2, n + 1):
        fib_array.insert(i, fib_array[i-1] + fib_array[i-2])

    return fib_array[n]

print(f"Fibonacci clássico: {fib(5)}")
