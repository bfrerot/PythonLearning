# Determiner si on a un triangle 

def isItATriangle(a, b, c):
    if a + b <= c:
        print ("it cannot be a triangle")
        return False
        
    if b + c <= a:
        print ("it cannot be a triangle")
        return False
        
    if c + a <= b:
        print ("it cannot be a triangle")
        return False
            			
    return True
    print ("it is a triangle !")

print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
# it is a triangle !
# True
# it cannont be a triangle
# False


### OR simpler


def isItATriangle(a, b, c):
    if a + b > c and b + c > a and c + a > b == True:
        return ("it is a triangle")
    else:
        return ("it cannot be a triangle")
    
print(isItATriangle(1, 1, 1))
print(isItATriangle(1, 1, 3))
# it is a triangle
# it cannot be a triangle


### Determiner si on a un triangle à angle droit

def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if not isItATriangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    # pourquoi n'a-t-on pas besoin de la ligne avec b >a et c ????

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(1, 4, 3))

