# libraryをimport
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time
import os
import re
import string
from datetime import datetime, timedelta
from scipy.optimize import curve_fit
from scipy.optimize import least_squares
import scipy.optimize as so
import sympy as sym
sym.init_printing(use_unicode=False, wrap_line=True)

# データの読み込み
df = pd.read_csv('./data/wholetime.csv')

"""
model1の定義

Npを時間で可変し、kappaを一定とする
このモデルでkappaを非線形最小二乗法で推定する
"""
def model(m, m0, kappa):
    a = (1+np.sqrt(1+(32*m0/kappa)))/2
    res = a * (1 - (2/kappa*a)*(1-(1-kappa/2)**a))
    return res

# kappaを推定する
# 初期値
kappa = 0.2
# 最適化の範囲
bounds = ([0, 0], [1, np.inf])
# 最適化
res = so.curve_fit(model, df['time'], df['Np'], p0=[0.2], bounds=bounds)
# 推定値
kappa = res[0][0]
print('kappa:', kappa)

