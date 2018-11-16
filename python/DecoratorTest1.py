class Foo(object):
    @staticmethod
    def bar(self):
        pass


class stu(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __iter__(self):
        return self

    def t(self, code):
        if code in self:
            print('test1')
        else:
            print('no exist')
c = stu('a',12)
c.t('a')