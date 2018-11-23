# -*- encoding:utf-8 -*-
from collections import OrderedDict
from collections import namedtuple
from abupy import six, xrange, range, reduce, map, filter, partial
from abupy import ABuSymbolPd


price_array = ABuSymbolPd.make_kl_df('TSLA', n_folds=2).close.tolist()
date_array = ABuSymbolPd.make_kl_df('TSLA', n_folds=2).date.tolist()

class StockTradeDays(object):
    def __init__(self,price_array, start_date,date_array=None):
        self._price_array = price_array
        self._date_array = self._init_days(start_date,date_array)
        self._change_array = self._init_change()
        self._stock_dict = self._init_stock_dict()
    def _init_days(self, start_date,date_array):
        if date_array is None:
            date_array = [str(start_date+inx) for inx, _ in enumerate(self._price_array)]
        else:
            date_array = [str(d) for d in date_array]
        return date_array

    def _init_change(self):
        price_float_array = [float(p) for p in self._price_array]
        pp_array = [(p1, p2) for p1, p2 in zip(price_float_array[:-1], price_float_array[1:])]
        change_array = list(map(lambda pp: reduce(lambda a, b: round((b-a)/a, 3), pp), pp_array))
        change_array.insert(0, 0)
        return change_array

    def _init_stock_dict(self):
        stock_nametuple = namedtuple('stock', ['date', 'price', 'change'])

        stock_dict_new1 = OrderedDict((date, stock_nametuple(date, price, change)) for date,price, change in zip(self._date_array, self._price_array, self._change_array))

        return stock_dict_new1

    def filter_stock(self,want_up=True, want_cal_sum=False):
        if not isinstance(self._stock_dict, OrderedDict):
            raise TypeError("error type dict")

        filter_func = (lambda day: day.change > 0) if want_up else (lambda day: day.change < 0)

        filter_days = list(filter(filter_func, self._stock_dict.values()))
        print(filter_days)
        sum_change = float(0)

        if want_cal_sum:
            sum_change = reduce(lambda x, y: x.change + y.change, filter_days)
        return filter_days, sum_change

    def __str__(self):
        return str(self._stock_dict.values())

    def __len__(self):
        return len(self._stock_dict)

    def __iter__(self):
        for key in self._stock_dict:
            yield self._stock_dict[key]
    def __getitem__(self, ind):
        return self._stock_dict[self._date_array[ind]]



