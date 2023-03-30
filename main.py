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


#MEMOIZED-FIBO (f, n)
# para i ← 0 até n faça
#      f [i] ← −1
# devolva LOOKUP-FIBO (f, n)

#LOOKUP-FIBO (f, n)
# se f [n] ≥ 0
#     então devolva f [n]
# se n ≤ 1
# então f [n] ← n
# senão f [n] ← LOOKUP-FIBO(f, n − 1) + LOOKUP-FIBO(f, n − 2)
# devolva f [n]

def memoized_fibo(n):
    fib_array = list()

    for i in range(0, n + 1):
        fib_array.insert(i, -1)
    
    return lookup_fibo(fib_array, n)

def lookup_fibo(fib_array, n):
    current_element = fib_array[n]

    if(current_element >= 0):
        return current_element
    
    if(n <= 1):
        fib_array[n] = n
    else:
        fib_array[n] = lookup_fibo(fib_array, n - 1) + lookup_fibo(fib_array, n - 2)

    return fib_array[n]

print(f"Fibonacci memo: {memoized_fibo(5)}")
