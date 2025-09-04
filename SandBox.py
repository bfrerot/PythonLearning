# class decorator
def add_logging_and_repr(cls):
    orig_init = cls.__init__

    # wrapper sur l'initialisation pour logguer les créations
    def __init__(self, *args, **kwargs):
        print(f"Creating instance of {cls.__name__}")
        orig_init(self, *args, **kwargs)

    # donner une représentation lisible
    def __str__(self):
        return f"{cls.__name__}({', '.join(f'{k}={v}' for k, v in vars(self).items())})"

    cls.__init__ = __init__
    cls.__str__ = __str__
    return cls

@add_logging_and_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p)  
# Creating instance of Person
# Person(name=Alice, age=30)


