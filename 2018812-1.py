import ai_utils
from sklearn import datasets
import pandas as pd
import numpy as np

Species_dic = {
                0: 'Iris-setosa',       # 山鸢尾
                1: 'Iris-versicolor',   # 变色鸢尾
                2: 'Iris-virginica'     # 维吉尼亚鸢尾
}

iris = datasets.load_iris()
data = iris.data
target = iris.target

data1 = pd.DataFrame(data,columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
data1['Species'] = pd.Series(target).map(Species_dic)

ai_utils.do_pair_plot_for_iris(data1)