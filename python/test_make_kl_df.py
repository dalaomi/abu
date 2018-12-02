from abupy import ABuSymbolPd
# n_folds 历史数据年数
# 单个股票获取历史数据
tsla_df = ABuSymbolPd.make_kl_df('usTSLA', n_folds=2)
print(tsla_df.shape)
# DataFrame
#print(type(tsla_df))
print(tsla_df.head())
