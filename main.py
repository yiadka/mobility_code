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
from src import exploratory_data_analysis as eda
from src import modeling as md

def main():
    file_path = "/Users/yiadka/dev/mobility_code/data/wholetime.csv"
    print("=====================================")
    start = time.time()
    print("Loading the dataset...")
    df_left, df_right = dp.preprocess_data(file_path)
    elapsed_time = time.time() - start
    # elapsed_timeを小数点以下2桁で表示
    elapsed_time = round(elapsed_time, 2)
    print("Loading the dataset is completed.")
    print("Loading dataset elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print("=====================================")

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

    # N-M plotを作成
    # print("Creating N-M plot...")
    # eda.visualize_nm(node_left, edge_left)
    # eda.visualize_nm(node_right, edge_right)
    
    # Npを計算
    print("=====================================")
    print("Calculating Np...")
    Np = eda.calc_Np(edge_left, node_left)
    print("Np: ", Np)
    print("Calculating Np is completed.")
    print("=====================================")

if __name__ == "__main__":
    main()
    