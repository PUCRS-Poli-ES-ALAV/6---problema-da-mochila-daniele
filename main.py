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