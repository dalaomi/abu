from functools import reduce
from collections import namedtuple
import itertools
import numpy as np
import pandas as pd
data = np.arange(0, 16).reshape(4, 4)
print(data)
data = pd.DataFrame(data, columns=["0", "1", "2", "3"])
print(data)


def f(x):
    return x.max()
print(data.apply(f, axis=1))
