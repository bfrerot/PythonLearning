########## OOP - Summary ##########


class Duck:                                             # Class
    counter = 0                                         # Class variable, counter type
    species = 'duck'                                    # Class variable
    __type = "mammifere"                                # Class mangled variable

    def __init__(self, height, weight, sex):            # constructor, self + 3 parameters
        self.height = height                            # instance variable
        self.weight = weight                            # instance variable 
        self.sex = sex                                  # instance variable
        Duck.counter +=1                                # Class variable, counter type modification from method , here __init__

    def walk(self):                                     # method, self
        pass

    def quack(self):                                    # method, self
        print('quacks')

class Chicken:                                          # Class
    species = 'chicken'                                 # Class variable

    def walk(self):                                     # method, self
        pass

    def cluck(self):                                    # method, self
        print('clucks')

duckling = Duck(height=10, weight=3.4, sex="male")      # instance creation, 3*parameters needed
drake = Duck(height=25, weight=3.7, sex="male")         # instance creation, 3*parameters needed
hen = Duck(height=20, weight=3.4, sex="female")         # instance creation, 3*parameters needed

chicken = Chicken()                                     # instance creation, no parameter needed


print('So many ducks were born:', Duck.counter)         # access a Class variable
# So many ducks were born: 3

for poultry in duckling, drake, hen, chicken:           # access a Class variable 
    print(poultry.species, end=' ')
    if poultry.species == 'duck':
        poultry.quack()
    elif poultry.species == 'chicken':
        poultry.cluck()
# duck quacks
# duck quacks
# duck quacks
# chicken clucks

print(drake.sex)                                         # access an instance variable
# male
print(hen.height)                                        # access an instance variable
# 20
print(duckling._Duck__type)                              # access an instance mangled variable
# mammifere




#####################################################################################################################################################################################################################################################


class Phone:                                 # Class
    counter = 0                              # Class variable, counter type

    def __init__(self, number):              # constructor __init__, self + 1*parameter
        self.number = number                 # instance variable creation
        Phone.counter += 1                   # Class variable modification (+1)

    def call(self, number):                  # method, self + 1*parameter
        message = 'Calling {} using own number {}'.format(number, self.number)  # NO instance creation
        return message                       # action = returning a message


class FixedPhone(Phone):                     # Class, subclass of Class "Phone" -- Inheritance
    last_SN = 0                              # Class variable

    def __init__(self, number):              # constructor __init__, self + 1*parameter
        super().__init__(number)             # upper_class init ==> Upper Class variable modification (+1) ==> Phone.counter +=1
        FixedPhone.last_SN += 1              # Class variable modification (+1)
        self.SN = 'FP-{}'.format(FixedPhone.last_SN)  


class MobilePhone(Phone):                    # Class, subclass of Class "Phone" -- Inheritance
    last_SN = 0

    def __init__(self, number):              # constructor __init__, self + 1*parameter
        super().__init__(number)             # upper_class init ==> Upper Class variable modification (+1) ==> Phone.counter +=1
        MobilePhone.last_SN += 1             # Class variable modification (+1)
        self.SN = 'MP-{}'.format(MobilePhone.last_SN)


print('Total number of phone devices created:', Phone.counter)
# Total number of phone devices created: 0      
print(Phone.counter)                                     # access Class variable
# 0

fphone = FixedPhone('555-2368')
mphone = MobilePhone('01632-960004')

print('Total number of phone devices created:', Phone.counter)            # access Class variable
# Total number of phone devices created: 2
print('Total number of mobile phones created:', MobilePhone.last_SN)      # access Class variable
# Total number of mobile phones created: 1
print(Phone.counter)
# 2

print(fphone.call('01632-960004'))                          # instance method
# Calling 01632-960004 using own number 555-2368
print('Fixed phone received "{}" serial number'.format(fphone.SN))
# Fixed phone received "FP-1" serial number
print('Mobile phone received "{}" serial number'.format(mphone.SN))
# Mobile phone received "MP-1" serial number
