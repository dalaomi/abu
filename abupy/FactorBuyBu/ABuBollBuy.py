# -*- encoding:utf-8 -*-
"""
    买入择时示例因子：动态自适应双均线策略
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import math

import numpy as np

from .ABuFactorBuyBase import AbuFactorBuyXD, BuyCallMixin
from ..IndicatorBu.ABuNDMa import calc_ma_from_prices
from ..CoreBu.ABuPdHelper import pd_resample
from ..TLineBu.ABuTL import AbuTLine

__author__ = '阿布'
__weixin__ = 'abu_quant'


# noinspection PyAttributeOutsideInit
class ABuBollBuy(AbuFactorBuyXD, BuyCallMixin):
    """示例买入动态自适应双均线策略"""

    def _init_self(self, **kwargs):
        super(ABuBollBuy, self)._init_self(**kwargs)
        # 这里只是给个默认值，在这个策略里，这个值没什么卵用
        if 'xd' not in kwargs:
            # 如果外部没有设置xd值，默认给一个20
            kwargs['xd'] = 20
        # 在输出生成的orders_pd中显示的名字
        self.factor_name = '{}:'.format(self.__class__.__name__)

    def fit_month(self, today):
        pass

    def fit_day(self, today):
        """双均线买入择时因子，信号快线上穿慢行形成金叉做为买入信号"""

        self.kl_pd['MID'] = self.kl_pd['close'].rolling(window=20).mean().round(2)
        self.kl_pd['UPPER'] = self.kl_pd['MID'] + (self.kl_pd['close'].rolling(window=20).std(ddof=0) * 2).round(2)
        self.kl_pd['LOWER'] = self.kl_pd['MID'] - (self.kl_pd['close'].rolling(window=20).std(ddof=0) * 2).round(2)
        # 计算快线
        fast_line = self.xd_kl.macd_diff
        # 计算慢线
        slow_line = self.xd_kl.macd_dea
        if len(fast_line) >= 2 and len(slow_line) >= 2:
            # 今天的快线值
            fast_today = fast_line[-1]
            # 昨天的快线值
            fast_yesterday = fast_line[-2]
            # 今天的慢线值
            slow_today = slow_line[-1]
            # 昨天的慢线值
            slow_yesterday = slow_line[-2]

            if slow_yesterday >= fast_yesterday and fast_today > slow_today:
                # 快线上穿慢线, 形成买入金叉，使用了今天收盘价格，明天买入
                return self.buy_tomorrow()

    """可以选择是否覆盖AbuFactorBuyXD中的buy_tomorrow来增大交易频率，默认基类中self.skip_days = self.xd降低了频率"""
    # def buy_tomorrow(self):
    #     return self.make_buy_order(self.today_ind)
