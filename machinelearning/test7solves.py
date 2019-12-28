from scipy import stats
import numpy as np
import pandas as pd

df_time_1 = pd.read_csv('./data/time_bars_1.csv')
df_time_1['log_ret'] = np.log(df_time_1['close']).diff()
print(stats.jarque_bera(df_time_1['log_ret'].dropna()))
print(stats.kurtosis(df_time_1['log_ret'].dropna(), fisher=False))

df_time_2 = pd.read_csv('./data/time_bars.csv')
df_time_2['log_ret'] = np.log(df_time_2['close']).diff()
print(stats.jarque_bera(df_time_2['log_ret'].dropna()))
print(stats.kurtosis(df_time_2['log_ret'].dropna(), fisher=False))

df_dollar_1 = pd.read_csv('./data/dollar_bars.csv')
df_dollar_1['log_ret'] = np.log(df_dollar_1['close']).diff()
print(stats.jarque_bera(df_dollar_1['log_ret'].dropna()))
print(stats.kurtosis(df_dollar_1['log_ret'].dropna(), fisher=False))

df_dollar_2 = pd.read_csv('./data/dollar_bars_2.csv')
df_dollar_2['log_ret'] = np.log(df_dollar_2['close']).diff()
print(stats.jarque_bera(df_dollar_2['log_ret'].dropna()))
print(stats.kurtosis(df_dollar_2['log_ret'].dropna(), fisher=False))

