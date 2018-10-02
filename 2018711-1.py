import pandas as pd
import patsy
data = pd.DataFrame({
                    'x0':[1,2,3,4,5],
                    'x1':[0.01, -0.01,0.25,-4.1,0.],
                    'y':[-1.5,0.,3.6,1.3,-2.]
})
df1 = data.copy()
df = pd.DataFrame(data.values, columns=['one', 'two', 'three'])
df3 = df.copy()
df3['strings'] = ['a', 'b', 'c', 'd', 'e']
print(df3.values)
model_cols = ['x0', 'x1']
print(data.loc[:,model_cols].values)
data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'])
print(data)
dummies = pd.get_dummies(data.category, prefix='category')
print(dummies)
data_with_dummies = data.drop('category', axis=1).join(dummies)
print(data_with_dummies)

y, X = patsy.dmatrices('y ~ x0+x1', df1)
print(y)