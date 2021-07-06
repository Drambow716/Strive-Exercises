import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values

df['mean'] = df.mean(axis=1)

print(df)

df2 = df - df['mean']

print(df2)
