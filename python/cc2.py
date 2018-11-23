# -*- encoding:utf-8 -*-
from collections import OrderedDict
from collections import namedtuple
from abupy import six, xrange, range, reduce, map, filter, partial

price_array = ['30.14', '29.58', '26.36', '32.56', '32.82']
date_base = 20180101
date_array = [str(date_base+inx) for inx, _ in enumerate(price_array)]
stock_dict = OrderedDict((date, price) for date, price in zip(date_array,price_array))


def sample_2_2_1(stock_dict):
    price_float_array = [float(price) for price in stock_dict.values()]
    pp_array = [(p1, p2) for p1, p2 in zip(price_float_array[:-1], price_float_array[1:])]
    print(pp_array)
    change_array = list(map(lambda pp: reduce(lambda a, b: round((b - a)/a, 3), pp), pp_array))
    change_array.insert(0, 0)
    return change_array

change_array = sample_2_2_1(stock_dict)

stock_nametuple = namedtuple('stock',['date','price','change'])
stock_dict_new = OrderedDict((date,stock_nametuple(date, price, change)) for date, price, change
                             in zip(stock_dict.keys(),stock_dict.values(), change_array))
print(stock_dict_new)
# up_days = list(filter(lambda day: day.change>0, stock_dict_new.values()))


def filter_stock(stock_dict,want_up=True, want_cal_sum=False):
    if not isinstance(stock_dict, OrderedDict):
        raise TypeError("error type dict")

    filter_func = (lambda day:day.change>0) if want_up else (lambda day:day.change<0)

    filter_days = list(filter(filter_func, stock_dict.values()))
    print(filter_days)
    sum_change = float(0)

    if want_cal_sum:
        sum_change = reduce(lambda x, y: x.change+y.change, filter_days)
    return filter_days, sum_change


print(filter_stock(stock_dict_new, want_up=False, want_cal_sum=True))


for ind, dd in enumerate(stock_dict_new.values()):
    print(dd.change)

