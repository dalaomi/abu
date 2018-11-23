from functools import reduce
from collections import namedtuple
import itertools
func = lambda x: x+1
print(func(1))
print(func(2))
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print(list(filter(lambda x: (x % 3) == 0, foo)))
print(list(map(lambda x: x*2+10, foo)))
print(reduce(lambda x, y: x+y, foo))


stock_nametuple = namedtuple('stock', ['date', 'price', 'change'])


class stu(object):
    name = 'Student'


c = stu()

print(c.name)
print(stu.name)
c.name = 'NewStudent'

print(c.name)
print(stu.name)
del c.name
print(c.name)
print(stu.name)


items= [1, 2, 3]
for item in itertools.permutations(items):
    print(item)

for item in itertools.combinations(items, 2):
    print(item)

for item in itertools.combinations_with_replacement(items, 2):
    print(item)


ab = ['a', 'b']
cd = ['c', 'd']
for item in itertools.product(ab, cd):
    print(item)
