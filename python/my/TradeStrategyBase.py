# -*- encoding:utf-8 -*-
import six
from abc import ABCMeta, abstractmethod
from my.StockTradeDays import StockTradeDays
from functools import reduce
from concurrent.futures import ProcessPoolExecutor
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import my.Test
import itertools
from abupy import ABuSymbolPd
class TradeStrategyBase(six.with_metaclass(ABCMeta, object)):
    """
    abstract base class
    """
    @abstractmethod
    def buy_strategy(self, *args, **kwargs):
        pass

    @abstractmethod
    def sell_strategy(self, *args, **kwargs):
        pass


class TradeStrategy1(TradeStrategyBase):
    s_keep_stock_threshold = 20

    def __init__(self):
        self.keep_stock_day = 0
        self._buy_change_threshold = 0.07

    def buy_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_day.change > self._buy_change_threshold:
            #print("开始买入")
            self.keep_stock_day += 1
        elif self.keep_stock_day>0:
            #print("持有天数加1")
            self.keep_stock_day += 1

    def sell_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day > TradeStrategy1.s_keep_stock_threshold:
            #print("开始卖出")
            self.keep_stock_day = 0

    @property
    def buy_change_threshold(self):
        return self._buy_change_threshold

    @buy_change_threshold.setter
    def buy_change_threshold(self, buy_change_threshold):
        if not isinstance(buy_change_threshold, float):
            raise TypeError("buy_change_threshold type error")
        self._buy_change_threshold = round(buy_change_threshold, 2)


class TradeStrategy2(TradeStrategyBase):
    s_keep_stock_threshold = 10
    s_buy_change_threshold = -0.10

    def __init__(self):
        self.keep_stock_day = 0

    def buy_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day == 0 and trade_ind >= 1:
            #print("开始买入")

            today_down = trade_day.change < 0
            yestoday_down = trade_days[trade_ind - 1].change < 0
            total_change = trade_day.change + trade_days[trade_ind - 1].change
            if today_down and yestoday_down and total_change < self.s_buy_change_threshold:
                self.keep_stock_day += 1
        elif self.keep_stock_day>0:
            #print("持有天数加1")
            self.keep_stock_day += 1

    def sell_strategy(self, trade_ind, trade_day, trade_days):
        if self.keep_stock_day > TradeStrategy2.s_keep_stock_threshold:
            #print("开始卖出")
            self.keep_stock_day = 0
    @classmethod
    def set_keep_stock_threshold(cls, keep_stock_threshold):
        cls.s_keep_stock_threshold = keep_stock_threshold

    @staticmethod
    def set_buy_change_threshold(buy_change_threshold):
        TradeStrategy2.s_buy_change_threshold = buy_change_threshold





d = TradeStrategy2()
price_array = ABuSymbolPd.make_kl_df('TSLA', n_folds=2).close.tolist()
date_array = ABuSymbolPd.make_kl_df('TSLA', n_folds=2).date.tolist()

date_base = 20180101
c = StockTradeDays(price_array, date_base, date_array)
print("最后一天交易数据为:{}".format(c[-1]))
print("交易天数为:{}".format(len(c)))


class TradeLoopBack(object):
    def __init__(self, trade_days, trade_strategy):
        self.trade_days = trade_days
        self.trade_strategy = trade_strategy
        self.profit_array = []

    def execute_trade(self):
        for ind, day in enumerate(self.trade_days):
            if self.trade_strategy.keep_stock_day > 0:
                self.profit_array.append(day.change)

            if hasattr(self.trade_strategy, 'buy_strategy'):
                self.trade_strategy.buy_strategy(ind, day, self.trade_days)

            if hasattr(self.trade_strategy, 'sell_strategy'):
                self.trade_strategy.sell_strategy(ind, day, self.trade_days)


def calc(keep_stock_threshold, buy_change_threshold):
    tt = TradeStrategy2()
    tt.set_buy_change_threshold(buy_change_threshold)
    tt.set_keep_stock_threshold(keep_stock_threshold)
    trade_loop_back = TradeLoopBack(c, tt)
    trade_loop_back.execute_trade()
    # print(trade_loop_back.profit_array)
    return reduce(lambda x, y: x + y, trade_loop_back.profit_array), keep_stock_threshold, buy_change_threshold


print(calc(10,-0.10))

keep_stock_days = [day for day in range(1, 30) if day%2 == 0]
print(keep_stock_days)

buy_change_holds = [round((hold+5)/100*-1, 2) for hold in range(11)]
print(buy_change_holds)

result = []
for keep_stock_day, buy_change_hold in itertools.product(keep_stock_days, buy_change_holds):
    result.append(calc(keep_stock_day, buy_change_hold))
for p in sorted(result)[::-1][:10]:
    print(p)

# 该用多线程
def when_done(r):
    result.append(r.result())

result = []
with ProcessPoolExecutor() as pool:
    for keep_stock_day, buy_change_hold in itertools.product(keep_stock_days, buy_change_holds):
        future_result = pool.submit(calc, keep_stock_day, buy_change_hold)
        future_result.add_done_callback(when_done)
for p in sorted(result)[::-1][:10]:
    print(p)

