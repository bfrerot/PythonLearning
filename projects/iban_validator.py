# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')
print (iban)

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper() 
    print(iban) # 28233000015862778778528FR76
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
            print (iban2)
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
            print (iban2)
    iban = int(iban2)
    print(iban)
    if iban % 97 == 1: # is the remainder of the division of iban2 by 97 equal to 1?
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
    
    # FR76 2823 3000 0158 6277 8778 528
    