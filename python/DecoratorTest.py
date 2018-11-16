def debug01():
    import inspect
    call_name = inspect.stack()[1][3]
    print(inspect.stack()[1][3])
    print('[debug]:enter {}()'.format(call_name))

def debug02(func):
    def wrapper(*args, **kwargs):
        print('[DEBUG] enter {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

def debug03(level):
    def wrapper(func):
        def innerWrapper(*args, **kwargs):
            print('[{}] enter {}'.format(level, func.__name__))
            return func(*args, **kwargs)
        return innerWrapper
    return wrapper

@debug02
def sayHello():
    print('hello')

@debug03(level='INFO')
def sayGoodBye():
    print('hello')


class Test():
    def __call__(self):
        print('call me!')

t = Test()
t()  # call me


class logging(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[DEBUG]: enter function {func}()".format(func=self.func.__name__))
        return self.func(*args, **kwargs)
@logging
def say(something):
    print("say:{}".format(something))


class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value




man = Celsius(37)
print(man.to_fahrenheit())
print(man.__dict__)
man._temperature=100
print(man.get_temperature())



class Celsius1:
    def __init__(self, temperature=0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)
c = Celsius1(10)
print(c.__dict__)



class Celsius2:
    def __init__(self, temperature=0):
        self._temperature = temperature
    @staticmethod
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

cc = Celsius2(10)
print(cc.to_fahrenheit())
if __name__ == '__main__':
    #print(debug02(sayHello))
    #debug02(sayHello)()
    # sayGoodBye()
    sayHello()
    sayGoodBye()

    say("fuck")

