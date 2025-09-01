# Determiner la somme d'un produit factoriel

def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6): # testing
    print(n, factorialFun(n))
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120	
