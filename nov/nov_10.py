import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import optimize
from datetime import timedelta

# データセットを読み込む
df = pd.read_csv("../data/wholetime.csv")
df = df.dropna()

# データセットを分割する
