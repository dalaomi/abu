import sys, os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from abupy import ABuSymbolPd
from abupy.CoreBu import ABuEnv
from abupy.MarketBu import ABuDataFeed
from abupy.UtilBu import *
from abupy.AlphaBu import *
from abupy import AbuDoubleMaBuy
from abupy import AbuDoubleMaSell
from abupy import ABuBollBuy,ABuBollSell
import numpy as np
import pandas as pd
from abupy.TradeBu import *
cash = 1000000
#ABuEnv.g_private_data_source = ABuDataFeed.TXApi
ABuEnv.g_private_data_source = ABuDataFeed.TuShareApi

# 构建对比基准
#buy_factor_dict_list = list([{'class': AbuDoubleMaBuy, 'slow': 60, 'fast': 5}])
#sell_factor_dict_list = list([{'class': AbuDoubleMaSell, 'slow': 60, 'fast': 5}])
# 买入策略
buy_factor_dict_list = list([{'class': ABuBollBuy, 'xd': 60, 'fast': 5}])
# 卖出
sell_factor_dict_list = list([{'class': ABuBollSell, 'xd': 60, 'fast': 5}])
choice_symbols = list(["SZ000002"])
benchmark = AbuBenchmark("SZ000002")
capital = AbuCapital(cash, benchmark)
# AbuPickTimeWorker._day_task 核心逻辑
orders_pd, action_pd, _ = ABuPickTimeExecute.do_symbols_with_same_factors(choice_symbols,
                                                                          benchmark,
                                                                          buy_factor_dict_list,
                                                                          sell_factor_dict_list,
                                                                          capital, show=True)



# print(benchmark.kl_pd.index)
# index_array = np.array(["x1", "x2", "x3", "x4", "x5"])
# df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)), columns=['a', 'b', 'c', 'd', 'e'], index=index_array)
# print(df2)
# print(df2.loc[df2.index[0], "a"])



# def plus(df,n):
#     df['c'] = (df['a']+df['b'])
#     df['d'] = (df['a']+df['b']) * n
#     return df
# list1 = [[1,3],[7,8],[4,5]]
# df1 = pd.DataFrame(list1,columns=['a','b'])
# df1 = df1.apply(plus,axis=1,args=(2,))
# print(df1)
