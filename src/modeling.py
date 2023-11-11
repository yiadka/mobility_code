import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
from scipy import optimize
from datetime import timedelta
from scipy import stats
from scipy import special
from scipy import integrate

# 自作モジュール
from src import exploratory_data_analysis as eda
from src import data_preprocessing as dp

def model2(m, m0, Np):
    kappa = 8*m0/(Np**2-Np)
    res = Np*(1-2/(kappa*Np)*(1-(1-(kappa/2))**Np))
    return res
    
    
    
def model2_calc(node, edge):
    popt2, pcov2 = optimize.curve_fit(model2, edge, node)
    print("model2: ", popt2)
    N_fit2 = []
    M_fit2 = []
    Np2 = popt2[1]
    kappa2 = []
    for i in range(len(edge)):
        kappa2.append(8*edge[i]/(Np2**2-Np2))

    for i in range(len(node)):
        N_fit2.append(eda.calc_N(Np2, kappa2[i]))

    for i in range(len(edge)): 
        M_fit2.append(eda.calc_M(Np2, kappa2[i]))

    return N_fit2, M_fit2

def model_beta(x, a, Np, m):
    f = a**(x[0]-1) * (1-a)**(x[1]-1) / special.beta(x[0], x[1])
    sec_part = (1 - ((x[0] + x[1]) / x[0]) * 2*m*a / (Np**2 - Np))**(Np - 1)
    # fをaで微分
    ff = integrate.simps(f, a)
    return Np * (1 - ff * sec_part**(Np - 1))

def fitting(x, a, Np, m):
    popt, pcov = optimize.curve_fit(model_beta, x, m, p0=[a, Np, m])
    return popt

# 損失関数
def loss_func(x, a, Np, m):
    c = 0
    for i in np.arange(len(a)):
        p = model_beta(x, a[i], Np[i], m[i])
        c += (m[i] - p)**2
    return c

    

# https://qiita.com/katsu1110/items/5792250de638e377ee14