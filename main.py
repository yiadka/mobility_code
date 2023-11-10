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
from src import data_preprocessing as dp

def main():
    file_path = "/Users/yiadka/dev/mobility_code/data/wholetime.csv"
    
    start = time.time()
    print("Loading the dataset...")
    df_left, df_right = dp.preprocess_data(file_path)
    elapsed_time = time.time() - start
    # elapsed_timeを小数点以下2桁で表示
    elapsed_time = round(elapsed_time, 2)
    print("Loading the dataset is completed.")
    print("Loading dataset elapsed_time:{0}".format(elapsed_time) + "[sec]")

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

if __name__ == "__main__":
    main()
    