##########   Logical Bitwise


# Bitwise Operations in Python
# Bitwise operations work at the bit level (binary representation of numbers).


### & (Bitwise AND)
# Compares each bit of two numbers. If both bits are 1, the result is 1. Otherwise, it's 0.

a = 5  # (0101 in binary)
b = 3  # (0011 in binary)
print(a & b)  # 1 (0001 in binary)


### | (Bitwise OR)
# If at least one bit is 1, the result is 1.

print(a | b)  # 7 (0111 in binary)


### ^ (Bitwise XOR)
# Returns 1 if the bits are different.

print(a ^ b)  # 6 (0110 in binary)


### ~ (Bitwise NOT)
# Flips all bits (inverts the number).

print(~a)  # -6 (two's complement representation)
# think "steps"
#  0  1  2  3  4  5 = a
# -1 -2 -3 -4 -5 -6 = ~a


### << (Left Shift)
# Shifts bits left (multiplies by 2^n).

print(a << 1)  # 10 (1010 in binary)
# a = 5 = 0101
# (a << 1) = 1010 = 10
# (a << 2) = 10100 = 20


### >> (Right Shift)
# Shifts bits right (divides by 2^n).

print(a >> 1)  # 2 (0010 in binary)
# a = 5 0101
# (a >> 1) = 0010 = 2
# (a >> 2) = 0001 = 1


########## Deal with SINGLE bits

# Pour comprendre..

# exemple de variable sur laquelle on doit prendre 1 bit en considération pour notre tache/travail/etc
flag_register = 0x1234
# en binaire = 0000 0000 0000 0000 0001 0010 0011 0100 
# ordre des bits 31, 30, etc, 0, de gauche à droite
# on nous attribue le 3ème bit
# flag_register = 0000000000000000000000000000x000

### Checker l'état du bit
# on peut utiliser cette conjunction property:
# x & 1 = x
# x & 0 = 0
# on applique un bit mask au bit que l'on souhaite tester
# 00000000000000000000000000001000
# 0000000000000000000000000000x000
# si le résultat est True égal à 1 c'est que le bit esc activé
# sinon, le bit est False, égal à 0, désactivé

the_mask = 8 # = 0000 0000 0000 0000 0000 0000 0000 1000
if flag_register & the_mask:
    print ("My bit is set")
else:
    print ("My bit is NOT set")


### Reseter l'état du bit
flag_register = flag_register & ~the_mask
# ~the_mask = 1111 1111 1111 1111 1111 1111 1111 0111
flag_register &= ~the_mask


### Set le bit à 1
# x | 1 = 1
# x | 0 = x
flag_register = flag_register | the_mask
flag_register |= the_mask


### Inverser le bit
# x ^ 1 = ~x
# x ^ 0 = x
flag_register = flag_register ^ the_mask
flag_register ^= the_mask