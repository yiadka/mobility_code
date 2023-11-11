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

def calc_Np_beta(edge, node, alpha, beta):
    # a, Np, m, alpha, beta
    Np = max(node)
    initial_guess = [0.5, Np, 500, alpha, beta]
    # alphaとbetaを繰り返し変更して最適な値を求める
    popt, pcov = optimize.curve_fit(md.model_beta, edge, node, p0=initial_guess)
    Np = round(popt[1], 2)
    return Np

def estimate_Np_beta(edge, node):
    Np_list = []
    # alphaを0.01刻みで0から1まで変更
    for i in range(101):
        for j in range(101):
            Np_list.append(calc_Np_beta(edge, node, alpha=i/100, beta=j/100))
    
    max_Np = max(Np_list)
    return max_Np
