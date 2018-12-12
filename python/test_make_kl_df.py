from abupy import ABuSymbolPd
import talib
from abupy.CoreBu import ABuEnv
from abupy.MarketBu import ABuDataFeed
from abupy.UtilBu import *
import pandas as pd
import numpy as np
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
#tsla_df = ABuSymbolPd.make_kl_df('SH600281', start='2018-12-01')
# print(tsla_df.shape)
# DataFrame
#print(type(tsla_df))
#print(tsla_df.head())


# cuid = ABuStrUtil.create_random_with_num_low(40)
# print(cuid)
# cuid_md5 = ABuMd5.md5_from_binary(cuid)
# print(cuid_md5)
# random_suffix = ABuStrUtil.create_random_with_num(5)
# print(random_suffix)
print("------------")
# import  tushare as ts
# ts.set_token("b35e94151fe2561e2fbdc3cdde45c658623bc0deb171b67835e99ef3")
# pro = ts.pro_api()
# df = pro.daily(ts_code='600281.SH', start_date='20181201')
# print(df.head())
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

# s = pd.Series(range(3))
# print(s.rolling(min_periods=1,window=3,center=False).mean())
def myMACD(price, fastperiod=12, slowperiod=26, signalperiod=9):
    ewma12 = price.ewma(span=fastperiod)
    ewma60 = price.ewma(span=slowperiod)
    dif = ewma12-ewma60
    dea = pd.ewma(dif,span=signalperiod)
    bar = (dif-dea) #有些地方的bar = (dif-dea)*2，但是talib中MACD的计算是bar = (dif-dea)*1
    return dif,dea,bar

tsla_df = ABuSymbolPd.make_kl_df('SZ000002')
#print(type(tsla_df))
# inplace 是否在原目标执行排序 True：是，False：否
tsla_df.sort_values(by=['date'], inplace=True, ascending=True)
# tsla_df['MA_5'] = tsla_df['close'].rolling(window=5).mean()
# tsla_df['MA_20'] = tsla_df['close'].rolling(window=20).mean()
# tsla_df['MA_5_PRE'] = tsla_df['MA_5'].shift(1)
# tsla_df['MA_20_PRE'] = tsla_df['MA_20'].shift(1)
# tsla_df['BOLL_UP'] = tsla_df['MA_20'] + tsla_df['close'].rolling(window=20).std(ddof=0) * 2
# tsla_df['BOLL_DN'] = tsla_df['MA_20'] - tsla_df['close'].rolling(window=20).std(ddof=0) * 2
# tsla_df['EMA_12'] = talib.EMA(tsla_df['close'], 12)
# tsla_df['EMA_26'] = talib.EMA(tsla_df['close'], 26)
tsla_df['MACD_DIFF'] = (talib.EMA(tsla_df['close'], 12) - talib.EMA(tsla_df['close'], 26)).round(2)
tsla_df['MACD_DEA'] = talib.EMA(tsla_df['MACD_DIFF'], 9).round(2)
tsla_df['MACD'] = 2*(tsla_df['MACD_DIFF']-tsla_df['MACD_DEA'])


#print("--------")
#tsla_df['a'],tsla_df['b'],tsla_df['c'] =talib.MACD(tsla_df['close'].values, fastperiod=6, slowperiod=12, signalperiod=9)
#tsla_df['a'],tsla_df['b'],tsla_df['c'] =myMACD(tsla_df['close'])
#tsla_df['d'] = tsla_df['a']-tsla_df['b']

#print(tsla_df)
#print(tsla_df.filter(tsla_df["MA_60"]>tsla_df["MA_5"]))
#print(tsla_df[(tsla_df["MA_20"]<tsla_df["MA_5"]) & (tsla_df["MA_20_PRE"] >= tsla_df["MA_5_PRE"])])

print(tsla_df)
