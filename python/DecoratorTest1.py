from abupy.CoreBu.ABuFixes import six


class ReplaceInit(object):
    def __init__(self):
        pass

    def __call__(self, cls):
        if isinstance(cls,six.class_types):
            init = cls.__init__

            def wrapped(*args,**kwargs):
                print('test wrap')
                init(*args, **kwargs)

            cls.__init__ = wrapped
            wrapped.__name__ = '__init__'
            wrapped.deprecated_original = init
        return cls
@ReplaceInit
class School:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def pr(self):
        print("name={},price={}".format(self.name, self.price))

c = School('test',2)
c.pr()


