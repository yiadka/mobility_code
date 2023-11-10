"""Qiitaのアイデアを実装する

"""

# library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize

signal = [0, 0.1, 0.2, 0.4, 0.8]

accuracy = [0.5, 0.73, 0.83, 0.92, 0.99]

numoftrial = [50, 45, 40, 35, 30]

# def. model
def probabilityCorrect(x, signal):
    # x: parameter
    # signal: signal level

    return 0.5 + (0.5 - x[0])*(1 - np.exp(-(signal/x[1])**x[2]))

# def. loss function
def lossFunc(x, signal, accuracy, numoftrial):
    # x: parameter
    # signal: signal level
    # performance: performance
    # numoftrial: number of trial
    c = 0
    for n in np.arange(len(numoftrial)):
        p = probabilityCorrect(x, signal[n])
        c += numoftrial[n] * (accuracy[n] - p)**2

    return c

def loss_mle(x, signal, accuracy, numoftrial):
    # x: parameter
    # signal: signal level
    # performance: performance
    # numoftrial: number of trial
    c = 0
    for n in np.arange(len(numoftrial)):
        p = probabilityCorrect(x, signal[n])
        if 0 < p <= 1:
            c += -numoftrial[n] * (accuracy[n] * np.log(p) + (1 - accuracy[n]) * np.log(1 - p))
    return c

x0 = [0, 0.2, 1]
bound = [(0, None), (0.001, None), (0, None)]

params_LSE = optimize.minimize(lossFunc,x0,args=(signal,accuracy,numoftrial,),method='l-bfgs-b',\
                        jac=None, bounds=bound, tol=None, callback=None,\
                        options={'disp': None, 'maxls': 20, 'iprint': -1,\
                                 'gtol': 1e-05, 'eps': 1e-08, 'maxiter': 15000,\
                                 'ftol': 2.220446049250313e-09, 'maxcor': 10,\
                                 'maxfun': 15000})

params_MLE = optimize.minimize(loss_mle,x0,args=(signal,accuracy,numoftrial,),method='l-bfgs-b',\
                        jac=None, bounds=bound, tol=None, callback=None,\
                        options={'disp': None, 'maxls': 20, 'iprint': -1,\
                                 'gtol': 1e-05, 'eps': 1e-08, 'maxiter': 15000,\
                                 'ftol': 2.220446049250313e-09, 'maxcor': 10,\
                                 'maxfun': 15000})


# visualize
signals = np.linspace(0,0.8,100)
acc_mle = np.zeros(100)
acc_lse = np.zeros(100)

for i in np.arange(100):
    acc_mle[i] = probabilityCorrect(params_MLE.x,signals[i])
    acc_lse[i] = probabilityCorrect(params_LSE.x,signals[i])

fig = plt.figure()
fig.suptitle('psychometric function')

ax = fig.add_subplot(111)

ax.set_xlabel('signal strength')
ax.set_ylabel('performance')    
plt.plot(signal, accuracy, 'ko')
plt.plot(signals, acc_mle, '-b')
plt.plot(signals, acc_lse, '-r')
plt.show()

