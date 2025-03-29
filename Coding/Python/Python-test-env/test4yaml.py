import yaml
with open("test.yml") as louloute:
    result = yaml.load(louloute)
    print(result)
    type(result)