# -*- encoding:utf-8 -*-
"""
    卖出择时示例因子，双均线策略
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from .ABuFactorSellBase import AbuFactorSellXD, ESupportDirection
from ..IndicatorBu.ABuNDMa import calc_ma_from_prices

__author__ = '阿布'
__weixin__ = 'abu_quant'


class ABuBollSell(AbuFactorSellXD):
    """示例卖出双均线择时因子"""

    def _init_self(self, **kwargs):
        super(ABuBollSell, self)._init_self(**kwargs)
        # 这里只是给个默认值，在这个策略里，这个值没什么卵用
        if 'xd' not in kwargs:
            # 如果外部没有设置xd值，默认给一个20
            kwargs['xd'] = 20
        # 在输出生成的orders_pd中显示的名字
        self.factor_name = '{}:'.format(self.__class__.__name__)

    def support_direction(self):
        """支持的方向，因子支持两个方向"""
        return [ESupportDirection.DIRECTION_CAll.value, ESupportDirection.DIRECTION_PUT.value]

    def fit_day(self, today, orders):
        """
            双均线卖出择时因子：
            call方向：快线下穿慢线形成死叉，做为卖出信号
            put方向： 快线上穿慢线做为卖出信号
        """

        p = today.close
        up = today.high
        MID = today.MID
        UPPER = today.UPPER
        LOWER = today.LOWER
        for order in orders:
            if order.expect_direction == 1 \
                    and up >= UPPER:
                # call方向：快线下穿慢线线形成死叉，做为卖出信号
                self.sell_today(order)
            elif order.expect_direction == -1 \
                    and up >= UPPER:
                # put方向：快线上穿慢线做为卖出信号
                self.sell_today(order)

