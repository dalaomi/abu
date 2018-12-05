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
#ABuEnv.g_private_data_source = ABuDataFeed.TXApi
# 自定义tushare数据源
ABuEnv.g_private_data_source = ABuDataFeed.TuShareApi
tsla_df = ABuSymbolPd.make_kl_df('SH600281', start='2018-12-01')
# print(tsla_df.shape)
# DataFrame
#print(type(tsla_df))
print(tsla_df.head())


# cuid = ABuStrUtil.create_random_with_num_low(40)
# print(cuid)
# cuid_md5 = ABuMd5.md5_from_binary(cuid)
# print(cuid_md5)
# random_suffix = ABuStrUtil.create_random_with_num(5)
# print(random_suffix)
print("------------")
import  tushare as ts
ts.set_token("b35e94151fe2561e2fbdc3cdde45c658623bc0deb171b67835e99ef3")
pro = ts.pro_api()
df = pro.daily(ts_code='600281.SH', start_date='20181201')
print(df.head())
# print(type(df))
# print("-----")
# for index, item in df.iterrows():
#     print(item["open"])

# print(ABuDateUtil.begin_date(pre_days=1, split='-'))
# tmp_end = ABuDateUtil.current_str_date()
# end = tmp_end
# end = end.replace("-", "")
# print(tmp_end)
# print(end)
# print(ABuDateUtil.fmt_date(end))
