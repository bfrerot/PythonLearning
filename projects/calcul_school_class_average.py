## Calculer la moyenne des eleves par ordre alphabetique

schoolClass = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in schoolClass:
        schoolClass[name] += (score,)
    else:
        schoolClass[name] = (score,)
        
print (schoolClass)

for name in sorted(schoolClass.keys()):
    sum = 0
    counter = 0
    for score in schoolClass[name]:
        sum += score
        counter += 1
    print(name, ":", sum / counter)

# Enter the student's name (or type exit to stop): imane
# Enter the student's score (0-10): 8
# Enter the student's name (or type exit to stop): ouweys
# Enter the student's score (0-10): 7
# Enter the student's name (or type exit to stop): soumaya
# Enter the student's score (0-10): 9
# Enter the student's name (or type exit to stop): imane
# Enter the student's score (0-10): 7
# Enter the student's name (or type exit to stop): ouweys
# Enter the student's score (0-10): 10
# Enter the student's name (or type exit to stop): soumaya
# Enter the student's score (0-10): 7
# Enter the student's name (or type exit to stop): exit
# {'imane': (8, 7), 'ouweys': (7, 10), 'soumaya': (9, 7)}
# imane : 7.5
# ouweys : 8.5
# soumaya : 8.0