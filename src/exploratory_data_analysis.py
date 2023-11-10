import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_nm(node_list, edge_list):
    plt.figure(figsize=(12, 8))
    plt.scatter(node_list, edge_list)
    plt.xlabel("N")
    plt.ylabel("M")
    plt.xscale("log")
    plt.yscale("log")
    plt.title("N-M plot")
    plt.show()