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

def model_beta(x, a, Np, m):
    f = a**(x[0]-1) * (1-a)**(x[1]-1) / special.beta(x[0], x[1])
    sec_part = (1 - ((x[0] + x[1]) / x[0]) * 2*m*a / (Np**2 - Np))**(Np - 1)
    # fをaで微分
    ff = integrate.simps(f, a)
    return Np * (1 - ff * sec_part**(Np - 1))


 