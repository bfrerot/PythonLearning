# Calcul du BMI - simple

def bmi(weight, height):
    return weight / height ** 2

print(bmi(52.5, 1.65))
19.283746556473833


# Calcul du BMI - avec ajout d'une function de conversion lb to kg et feet to main

def ftintom(ft, inch = 0.0): # inch = 0.0 --> default value si aucune n'est donnée
    return ft * 0.3048 + inch * 0.0254

def lbstokg(lb):
    return lb * 0.45359237

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200: # Condition d'exclusion
        return None
    
    return weight / height ** 2

print(bmi(weight = lbstokg(176), height = ftintom(5, 7)))
27.565214082533313