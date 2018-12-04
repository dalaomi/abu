from abupy import ABuSymbolPd
from abupy.CoreBu import ABuEnv
from abupy.MarketBu import ABuDataFeed
# n_folds 历史数据年数
# 单个股票获取历史数据
"""
    1、核心代码：kline_pd，支持先从本地获取，若不存在，从网络数据源获取
    2、数据源默认为百度
    3、自定义数据源必须复写BaseMarket
"""
# ABuEnv.g_private_data_source = ABuDataFeed.TXApi
tsla_df = ABuSymbolPd.make_kl_df('usTSLA', n_folds=2)
print(tsla_df.shape)
# DataFrame
#print(type(tsla_df))
print(tsla_df.head())

