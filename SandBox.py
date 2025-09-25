import json                          # import json module

class Who:                           # create class "Who"
    def __init__(self, name, age):   # 2*args mandatory
        self.name = name
        self.age = age

class MyEncoder(json.JSONEncoder):    # create a Class which inherits from json.JSONEncoder Class
    def default(self, w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            return super().default(self, w)

class MyDecoder(json.JSONDecoder):    # create a Class which inherits from json.JSONDecoder Class
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Who(**d)


some_man = Who('Jane Doe', 23)    # create an instance of Class "Who"
print(some_man)
# <__main__.Who object at 0x000001D1FFB92E40>
print(some_man.name)
# Jane Doe
print(some_man.age)
# 23

json_str = json.dumps(some_man, cls=MyEncoder)   # build a JSON format dict/object
print(type(json_str))
# <class 'str'>     # it is now seen as a "string" by Python !
print(json_str)
# {"name": "Jane Doe", "age": 23}

new_man = json.loads(json_str, cls=MyDecoder)
print(type(new_man))
# <class '__main__.Who'>
print(new_man.__dict__)
# {'name': 'Jane Doe', 'age': 23}                # rebuild in Python format