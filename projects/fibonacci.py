# Afficher les nombres de Fibonacci --> Fib(i) = Fib(i-1) + Fib(i-2)
def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    sum = 0
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fib(n))
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13
# 8 -> 21
# 9 -> 34


### OR simpler

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2) #
for n in range(1, 10):
    print(n, "->", fib(n))
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13
# 8 -> 21
# 9 -> 34