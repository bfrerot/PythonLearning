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
    
    
    ########################################################################################################################################
    
    
class IBANValidationError(Exception):
    pass


def validateIBAN(iban):
    iban = iban.replace(' ', '')

    if not iban.isalnum():
        raise IBANValidationError("You have entered invalid characters.")

    elif len(iban) < 15:
        raise IBANValidationError("IBAN entered is too short.")

    elif len(iban) > 31:
        raise IBANValidationError("IBAN entered is too long.")

    else:
        iban = (iban[4:] + iban[0:4]).upper()
        iban2 = ''
        for ch in iban:
            if ch.isdigit():
                iban2 += ch
            else:
                iban2 += str(10 + ord(ch) - ord('A'))
        ibann = int(iban2)

        if ibann % 97 != 1:
            raise IBANValidationError("IBAN entered is invalid.")

        return True


test_keys = ['GB72 HBZU 7006 7212 1253 01', 'FR76 30003 03620 00020216907 50', 'DE02100100100152517108' ]

for key in test_keys:
    try:
        print('Status of "{}" validation: '.format(key))
        validateIBAN(key)
    except IBANValidationError as e:
        print("\t{}".format(e))
    else:
        print("\tcorrect")


########################################################################################################################################



    