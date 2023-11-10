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

# Nを計算する
def calc_N(Np, kappa):
    return Np * (1 - (2 / (kappa * Np))*(1 - (1 - (kappa / 2))**Np))

# Mを計算する
def calc_M(Np, kappa):
    return (kappa * Np * (Np - 1)) / 8

