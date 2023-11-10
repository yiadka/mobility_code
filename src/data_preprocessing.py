import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
from datetime import timedelta
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
import time

# 自作モジュール
from src import return_nmdt as rn

def load_data(file_name):
    df = pd.read_csv(file_name)
    df = df.dropna()
    return df

def preprocess_data(data):
    df = pd.read_csv(data)
    df = df.dropna()

    df_p1 = df[(df['started_at'] >= '2020-03-01') & (df['started_at'] < '2020-06-01')].dropna()
    df_p2 = df[(df['started_at'] >= '2020-06-01') & (df['started_at'] < '2020-11-01')].dropna()
    df_p3 = df[(df['started_at'] >= '2020-12-01') & (df['started_at'] < '2021-03-01')].dropna()
    df_p4 = df[(df['started_at'] >= '2021-03-01') & (df['started_at'] < '2023-10-01')].dropna()
    df_p4_1 = df[(df['started_at'] >= '2021-03-01') & (df['started_at'] < '2022-01-01')].dropna()
    df_p4_2 = df[(df['started_at'] >= '2022-01-01') & (df['started_at'] < '2023-10-01')].dropna()
    df_left = pd.concat([df_p1, df_p2, df_p3, df_p4_1], axis=0)
    df_right = pd.concat([df_p4_2], axis=0)

    return df_left, df_right