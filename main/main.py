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
import return_nmdt as rn

# あとでリファクタリング

if __name__ == "__main__":
    # データセットを読み込む
    # データセットを読み込む際に、プログレスバーを表示する
    print("Loading the dataset...")
    start = time.time()
    df = pd.read_csv("data/wholetime.csv")
    df = df.dropna()
    print("Loading the dataset is completed.")
    elapsed_time = time.time() - start
    # elapsed_timeを小数点以下2桁で表示
    elapsed_time = round(elapsed_time, 2)
    print("Loading dataset elapsed_time:{0}".format(elapsed_time) + "[sec]")

    # データセットを分割する
    print("Splitting the dataset...")
    start = time.time()
    df_p1 = df[(df['started_at'] >= '2020-03-01') & (df['started_at'] < '2020-06-01')].dropna()
    df_p2 = df[(df['started_at'] >= '2020-06-01') & (df['started_at'] < '2020-11-01')].dropna()
    df_p3 = df[(df['started_at'] >= '2020-12-01') & (df['started_at'] < '2021-03-01')].dropna()
    df_p4 = df[(df['started_at'] >= '2021-03-01') & (df['started_at'] < '2023-10-01')].dropna()
    df_p4_1 = df[(df['started_at'] >= '2021-03-01') & (df['started_at'] < '2022-01-01')].dropna()
    df_p4_2 = df[(df['started_at'] >= '2022-01-01') & (df['started_at'] < '2023-10-01')].dropna()
    df_left = pd.concat([df_p1, df_p2, df_p3, df_p4_1], axis=0)
    df_right = pd.concat([df_p4_2], axis=0)
    print("Splitting the dataset is completed.")
    elapsed_time = time.time() - start
    # elapsed_timeを小数点以下2桁で表示
    elapsed_time = round(elapsed_time, 2)
    print("Splitting elapsed_time:{0}".format(elapsed_time) + "[sec]")

    # df_leftのノード数とエッジ数を取得
    print("Getting the number of nodes and edges...")
    start = time.time()
    node_left, edge_left, timestamp_left = rn.return_nm(df_left)
    # df_rightのノード数とエッジ数を取得
    node_right, edge_right, timestamp_right = rn.return_nm(df_right)
    print("Getting the number of nodes and edges is completed.")
    elapsed_time = time.time() - start
    # elapsed_timeを小数点以下2桁で表示
    elapsed_time = round(elapsed_time, 2)
    print("Getting elapsed_time:{0}".format(elapsed_time) + "[sec]")

    # ノード数とエッジ数をプロット
    plt.figure(figsize=(12, 8))
    plt.scatter(node_left, edge_left, label="left")
    plt.scatter(node_right, edge_right, label="right")
    plt.xlabel("N")
    plt.ylabel("M")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("N-M plot")
    plt.legend()
    # plt.savefig("/fig/nov_10.png")
    plt.show()