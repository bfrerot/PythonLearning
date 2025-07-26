########## MATH MODULE ##########


# MATH module comes with the standard Python release, and contains some useful constants and functions for carrying out mathematical operations
# Note: all trigonometrical functions take their arguments expressed in radians
import math

## math.pi 
# = π constant value


## math.e 
# Euler's number value



### Racine carrée

## math.sqrt(x) 
# racine carrée de x

print(math.sqrt(16))    
# 4.0
print(math.sqrt(25))    
# 5.0
print(math.sqrt(2))     
# 1.4142135623730951



### fonctions trigonométriques de base

## math.sin(x) 
# sine of x

print(math.sin(0))              
# 0.0
print(math.sin(math.pi/2))      
# 1.0 (90 degrés)


## math.cos(x) 
# cosine of x

print(math.cos(0))              
# 1.0
print(math.cos(math.pi))        
# -1.0 (180 degrés)


## math.tan(x) 
# the tangent of x

print(math.tan(0))              
# 0.0
print(math.tan(math.pi/4))      
# 1.0 (45 degrés)



### fonctions trigonométriques inverses

## math.asin(x) 
# arcsine of x

print(math.asin(0))     
# 0.0
print(math.asin(1))     
# 1.5707963267948966 (π/2)


## math.acos(x) 
# arccosine of x

print(math.acos(1))     
# 0.0
print(math.acos(0))     
# 1.5707963267948966 (π/2)


## math.atan(x) 
# arctangent of x

print(math.atan(0))     
# 0.0
print(math.atan(1))     
# 0.7853981633974483 (π/4)



### conversions degrés/radians

## math.radians(x) 
# convertit degrés en radians

print(math.radians(90))     
# 1.5707963267948966 (π/2)
print(math.radians(180))    
# 3.141592653589793 (π)
print(math.radians(360))    
# 6.283185307179586 (2π)


## math.degrees(x) 
# convertit radians en degrés

print(math.degrees(math.pi))    
# 180.0
print(math.degrees(math.pi/2))  
# 90.0



### Fonctions hyperboliques

## math.sinh(x) 
# hyperbolic sine

print(math.sinh(0))     
# 0.0
print(math.sinh(1))     
# 1.1752011936438014


## math.cosh(x) 
# hyperbolic cosine

print(math.cosh(0))     
# 1.0
print(math.cosh(1))     
# 1.5430806348152437


## math.tanh(x) 
# hyperbolic tangent

print(math.tanh(0))     
# 0.0
print(math.tanh(1))     
# 0.7615941559557649



### Fonctions hyperboliques inverses

## math.asinh(x) 
# hyperbolic arcsine

print(math.asinh(0))    
# 0.0
print(math.asinh(1))    
# 0.8813735870195429


## math.acosh(x) 
# hyperbolic arccosine
# (x ≥ 1)

print(math.acosh(1))    
# 0.0
print(math.acosh(2))    
# 1.3169578969248166


## math.atanh(x) 
# hyperbolic arctangent
# (-1 < x < 1)

print(math.atanh(0))    
# 0.0
print(math.atanh(0.5))  
# 0



### Fonction exponentielle

## math.exp(x) 
# finds the value of ex

print(math.exp(0))      
# 1.0 (e^0)
print(math.exp(1))      
# 2.718281828459045 (e^1 = e)
print(math.exp(2))      
# 7.38905609893065 (e^2)
print(math.exp(-1))     
# 0.36787944117144233 (e^-1)



### Fonctions logarithmiques

## math.log(x) 
# natural logarithm of x

print(math.log(1))      
# 0.0
print(math.log(math.e)) 
# 1.0
print(math.log(10))     
# 2.302585092994046


## math.log(x, b) 
# logarithm of x to base b

print(math.log(8, 2))   
# 3.0 (log₂(8) = 3 car 2³ = 8)
print(math.log(100, 10)) 
# 2.0 (log₁₀(100) = 2)
print(math.log(27, 3))  
# 3.0 (log₃(27) = 3)


## math.log10(x) 
# decimal logarithm of x (more precise than math.log(x, 10))

print(math.log10(10))   
# 1.0
print(math.log10(100))  
# 2.0
print(math.log10(1000)) 
# 3.0


## log2(x) 
# binary logarithm of x (more precise than math.log(x, 2))
print(math.log2(2))     
# 1.0
print(math.log2(8))     
# 3.0
print(math.log2(16))    
# 4.0



### Fonctions d'arrondi

## math.ceil(x) 
# ceiling of x, plus petit entier ≥ x

print(math.ceil(4.1))   
# 5
print(math.ceil(4.9))   
# 5
print(math.ceil(-4.1))  
# -4
print(math.ceil(4.0))   
# 4


## math.floor(x) 
# floor of x, plus grand entier ≤ x

print(math.floor(4.1))  
# 4
print(math.floor(4.9))  
# 4
print(math.floor(-4.1)) 
# -5
print(math.floor(4.0))  
# 4


## math.trunc(x) 
# value of x truncated to an integer 
# not an equivalent of either ceil or floor
# troncature (supprime la partie décimale)

print(math.trunc(4.9))  
# 4
print(math.trunc(-4.9)) 
# -4
print(math.trunc(4.0))  
# 4



### Factorielle

## math.factorial(x) 
# returns x! 
# x MUST be an INTEGER and POSITIVE

print(math.factorial(0))    
# 1
print(math.factorial(1))    
# 1
print(math.factorial(3))    
# 6 (3! = 3×2×1)
print(math.factorial(5))    
# 120 (5! = 5×4×3×2×1)
print(math.factorial(10))   
# 3628800

# dans un code
print(math.factorial( -3.0 ))
# TypeError: 'float' object cannot be interpreted as an integer
# Python voit le - avent de voir le .,

print(math.factorial( 3.0 ))
# TypeError: 'float' object cannot be interpreted as an integer

print(math.factorial( -3))
# ValueError: factorial() not defined for negative values


### Hypoténuse

## math.hypot(x, y) 
# returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y 
# the same as math.sqrt(pow(x, 2) + pow(y, 2)) but more precise

print(math.hypot(3, 4))     
# 5.0 (triangle 3-4-5)
print(math.hypot(1, 1))     
# 1.4142135623730951 (√2)
print(math.hypot(5, 12))    
# 13.0 (triangle 5-12-13)