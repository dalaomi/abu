# -*- encoding:utf-8 -*-
from abupy.WidgetBu import ABuWGBase
from abupy.UtilBu import ABuStrUtil
result_dict = ABuWGBase.search_to_symbol_dict('BABA', fast_mode=True)
print(result_dict)
result_options = [u'{}:{}'.format(ABuStrUtil.to_unicode(result_dict[symbol]), ABuStrUtil.to_unicode(symbol)) for symbol in result_dict]
print(result_options)
