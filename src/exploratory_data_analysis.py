import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize

# 自作モジュール
from src import modeling as md

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

def calc_Np(edge, node):
    # model2を用いてNpを計算
    # NLSを用いてNpを計算
    initial_guess = [1000, 100]
    popt, pcov = optimize.curve_fit(md.model2, edge, node, p0=initial_guess)
    Np = round(popt[1], 2)
    return Np

def calc_Np_beta(edge, node):
    initial_guess = [0.1, 1000, 100, 1, 1]
    popt, pcov = optimize.curve_fit(md.model_beta, edge, node, p0=initial_guess)
    Np = round(popt[1], 2)
    return Np

