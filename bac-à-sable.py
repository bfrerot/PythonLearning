class Package:
    spam = ""

    def __init__(self, content):
        Package.spam += content + ";"

envelope_1 = Package("Capacitors")
envelope_2 = Package("Transistors")
print(envelope_1.spam)
