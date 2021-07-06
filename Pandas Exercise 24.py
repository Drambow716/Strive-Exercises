import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))

sums = df.sum()

min_sum = sums.min()

print(sums[sums == min_sum].index[0])
