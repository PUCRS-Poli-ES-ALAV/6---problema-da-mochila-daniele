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

print(fib_rec(5))

#FIBO (n)
#     f [0] ← 0 
# f [1] ← 1
# para i ← 2 até n faça
#        f[i] ← f[i-1]+f[i-2]
# devolva f [n]

fib = []

def fib(n);
    fib[0] = 0
    fib[1] = 1

    for i in range(2..n):
        fib[i] = fib[i-1] + fib[i-2]

    return f[n]
