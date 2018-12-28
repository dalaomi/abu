class Indicator(object):
    def __init__(self, name, func, freq, win_size):
        self.name = name
        self.func = func
        self.freq = freq
        self.win_size = win_size
g_indicator = {}


def reg_indicator(name,func,freq,win_size):
    value = Indicator(name, func, freq, win_size)
    g_indicator[name] = value