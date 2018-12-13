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


class ABuMacdSell(AbuFactorSellXD):
    """示例卖出双均线择时因子"""

    def _init_self(self, **kwargs):
        super(ABuMacdSell, self)._init_self(**kwargs)
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

            for order in orders:
                if order.expect_direction == 1 \
                        and fast_yesterday >= slow_yesterday and fast_today < slow_today:
                    # call方向：快线下穿慢线线形成死叉，做为卖出信号
                    self.sell_tomorrow(order)
                elif order.expect_direction == -1 \
                        and slow_yesterday >= fast_yesterday and fast_today > slow_today:
                    # put方向：快线上穿慢线做为卖出信号
                    self.sell_tomorrow(order)
