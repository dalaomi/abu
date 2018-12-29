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

        # 为fit_day中截取昨天
        yesterday = self.kl_pd.iloc[self.today_ind - 1]
        # 为fit_day中截取前天
        bf_yesterday = self.kl_pd.iloc[self.today_ind - 2]
        p = today.close
        p_yesterday = yesterday.close
        l_yesterday = yesterday.low
        lower_yesterday = yesterday.LOWER
        # print(today.date, l_yesterday, p)
        MID = today.MID
        UPPER = today.UPPER
        LOWER = today.LOWER

        if l_yesterday <= lower_yesterday and p > LOWER:
            return self.buy_tomorrow()

    """可以选择是否覆盖AbuFactorBuyXD中的buy_tomorrow来增大交易频率，默认基类中self.skip_days = self.xd降低了频率"""
    # def buy_tomorrow(self):
    #     return self.make_buy_order(self.today_ind)
