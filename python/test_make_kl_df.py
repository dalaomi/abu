from abupy import ABuSymbolPd
from abupy.CoreBu import ABuEnv
from abupy.MarketBu import ABuDataFeed
from abupy.UtilBu import *
# n_folds 历史数据年数
# 单个股票获取历史数据
"""
    1、核心代码：kline_pd，支持先从本地获取，若不存在，从网络数据源获取
    2、数据源默认为百度
    3、自定义数据源必须复写BaseMarket
"""
ABuEnv.g_private_data_source = ABuDataFeed.TXApi
tsla_df = ABuSymbolPd.make_kl_df('usTSLA', n_folds=2)
print(tsla_df.shape)
# DataFrame
#print(type(tsla_df))
print(tsla_df.head())


cuid = ABuStrUtil.create_random_with_num_low(40)
print(cuid)
cuid_md5 = ABuMd5.md5_from_binary(cuid)
print(cuid_md5)
random_suffix = ABuStrUtil.create_random_with_num(5)
print(random_suffix)

import  tushare as ts
ts.set_token("b35e94151fe2561e2fbdc3cdde45c658623bc0deb171b67835e99ef3")
pro = ts.pro_api()
df = pro.daily(ts_code='000063.SZ', start_date='20180701', end_date='20180718')
print(df)