import numpy as np
from scipy.optimize import curve_fit

def getInitialValuesForModel1(node, edge, model1):
    # 初期値を探す for model2
    # 初期値の範囲を設定
    init_m0_range = [2, 1000]
    init_Np_range = [1, 1000]


    best_fit = None
    best_error = np.inf

    # ランダムな初期値で最適化を複数回実行
    for _ in range(100):
        init_m0 = np.random.uniform(*init_m0_range)
        init_Np = np.random.uniform(*init_Np_range)
        

        popt, pcov = curve_fit(model1, edge, node, p0=[init_m0, init_Np])

        # フィットの良さ（二乗誤差）を計算
        residuals = node - model1(edge, *popt)
        error = np.sum(residuals**2)

        # 最良のフィットを更新
        if error < best_error:
            best_error = error
            best_fit = popt

    # print(best_fit2)
    m0_init = best_fit[0]
    Np_init = best_fit[1]

    return m0_init, Np_init