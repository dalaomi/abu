def Decorator(obj):
    print('desc obj')
    obj.name ='test'
    def price():
        pass
    obj.price = price
    return obj

@Decorator
class School():
    def __init__(self, name, price):
        self.name = name
        self.price = price

c = School('a',12)
print(School.__dict__)
