import numpy as np
import pandas as pd

values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
print(pd.value_counts(values))
df = pd.DataFrame({
	'basket_id':np.arange(8),
	'fruit':values,
	'count':np.random.randint(3,15,8),
	'weight':np.random.uniform(0, 4, 8)
	},columns=['basket_id', 'fruit', 'count', 'weight'])
print(df)

categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]
my_cats_2 = pd.Categorical.from_codes(codes, categories)
print(my_cats_2)
rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts.resample('M').sum())