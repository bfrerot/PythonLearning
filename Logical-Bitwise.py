##########   Logical Operations in Python

# Logical operations work with boolean values (True and False). 
# The main logical operators in Python are:


###  and (Logical AND)
# Returns True if both operands are True.Otherwise, returns False.

print(True and True)   # True
print(True and False)  # False
print(False and False) # False


### or (Logical OR)
# Returns True if at least one operand is True. Returns False only if both operands are False.

print(True or False)   # True
print(False or False)  # False
print(True or True)    # True


### not (Logical NOT)
# Reverses the boolean value.

print(not True)  # False
print(not False) # True



########## Bitwise Operations in Python

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