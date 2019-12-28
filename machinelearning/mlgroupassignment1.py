
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
import numpy as np
import pandas as pd
from math import ceil
import cython
import cython_loops

df = pd.read_csv('./data/ES_Trades.csv')
print(df.head())

def __pre_process(data):
    # Create an date time
    data['Date_Time'] = data['Date'] + ' ' + data['Time']
    data = data.drop(['Date', 'Time'], axis=1)

    # Calculate the transaction value
    data['Transaction'] = data['Price'] * data['Volume']

    return data

data = __pre_process(df)
data['Group'] = np.nan
print(data.head())

def __extract_data(data):
    # Extract data
    date_time = data[['Date_Time', 'Group']].groupby('Group')['Date_Time'].last()
    ohlc = data[['Price', 'Group']].astype(float).groupby('Group')['Price'].ohlc()
    volume = data[['Volume', 'Group']].astype(float).groupby('Group').sum()
    vwap = pd.DataFrame(data[['Transaction', 'Group']].astype(float).groupby('Group').sum().values / volume.values)

    # Create DataFrame
    bars = pd.concat([date_time, ohlc, volume, vwap], axis=1)
    bars.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'vwap']

    return bars

def __time_bars(data, units):
    # Set the time frame
    duration = str(units) + 'T'

    # Extract data
    data.index = pd.to_datetime(data['Date_Time'])
    ohlc = data.resample(duration, label='right')['Price'].ohlc()
    date_time = pd.DataFrame(ohlc.index, index=ohlc.index)
    volume = data.resample(duration, label='right')['Volume'].sum()
    vwap = data.resample(duration, label='right')['Transaction'].sum().values / volume

    # Create DataFrame
    data = pd.concat([date_time, ohlc, volume, vwap], axis=1)
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'vwap']

    return data


def __dollar_bars(data, units):
    # Dollar metric
    data['CumDollars'] = data['Transaction'].cumsum()
    col_names = data.columns

    # Set the relevant group for each row
    data = cython_loops.set_row_groups(units, np.array(data))
    data = pd.DataFrame(data, columns=col_names)
    data = __extract_data(data)

    return data


def __volume_bars(data, units):
    # Volume metric
    data['CumVol'] = data['Volume'].cumsum()
    col_names = data.columns

    # Set the relevant group for each row
    data = cython_loops.set_row_groups(units, np.array(data))
    data = pd.DataFrame(data, columns=col_names)
    data = __extract_data(data)

    # Todo: Add 1/50 of the daily traded volume
    return data


def __tick_bars(data, units):
    # Create groups based on number of tick bars
    group_index = data.index % units == 0
    group_size = ceil(data.shape[0] / float(units))
    groups = np.array(range(0, int(group_size)))

    # Fill in group values
    data.loc[group_index, 'Group'] = groups
    data['Group'] = data['Group'].ffill()
    data = __extract_data(data)

    return data

def create_bars(data, units=1000, type='tick'):
    """
    Creates the desired bars. 4 different types:
    1. Time Bars
    2. Tick Bars
    3. Volume Bars
    4. Dollar Bars
    See book for more info:
    Marcos Prado (2018), Advances in Financial Machine Learning, pg 25
    :param data: Pandas DataFrame of Tick Data from TickData.com
    :param units: Number of units in a bar.
                  Time Bars: Number of minutes per bar
                  Tick Bars: Number of ticks per bar
                  Volume Bars: Number of shares traded per bar
                  Dollar Bars: Transaction size traded per bar
    :param type: String of the bar type, ('tick', 'volume', 'dollar', 'time')
    :return: Pandas DataFrame of relevant bar data
    """
    data = __pre_process(data)

    # Create an empty column
    data['Group'] = np.nan

    print('Creating {type} bars'.format(type=type))
    if type == 'tick':
        bars = __tick_bars(data, units)
    elif type == 'volume':
        bars = __volume_bars(data, units)
    elif type == 'dollar':
        bars = __dollar_bars(data, units)
    elif type == 'time':
        bars = __time_bars(data, units)
    else:
        raise ValueError('Type must be: tick, volume, dollar, or time')

    return bars

print('Uncomment time_bars in main.py if you want them to be created.')
#time_bars = create_bars(df, units=600, type='time')  # Time bars take long to run since I have not optimised them.
tick_bars = create_bars(df, units=5000, type='tick')
volume_bars = create_bars(df, units=21731, type='volume')
dollar_bars = create_bars(df, units=35638840, type='dollar')

def count_bars(data, price_col='close'):
    data['date'] = pd.to_datetime(data['date'])
    return data.groupby(pd.Grouper(key='date', freq='1W', axis=1))[price_col].count()

def scale(s):
    return (s-s.min())/(s.max()-s.min())


# count series
# scale to compare 'apples to apples'
time_bars_count = scale(count_bars(time_bars))
tick_bars_count = scale(count_bars(tick_bars))
volume_bars_count = scale(count_bars(volume_bars))
dollar_bars_count = scale(count_bars(dollar_bars))

# plot time series of count
fig,ax = plt.subplots(figsize=(10,7))

time_bars_count.plot(ax=ax, ls='-', label='time count')
tick_bars_count.plot(ax=ax, ls='--', label='tick count')
volume_bars_count.plot(ax=ax, ls='-.', label='volume count')
dollar_bars_count.plot(ax=ax, ls=':', label='dollar count')

ax.set_title('scaled bar counts')
ax.legend()

bar_types = ['time', 'tick','volume','dollar']
bar_std = [time_bars_count.std(),tick_bars_count.std(),volume_bars_count.std(),dollar_bars_count.std()]
counts = (pd.Series(bar_std,index=bar_types))
counts.sort_values()

print(f'time bar std: {time_bars_count.std():.2%}, tick bar std: {tick_bars_count.std():.2%}, volume bar std: {volume_bars_count.std():.2%}, dollar bar std: {dollar_bars_count.std():.2%}')

def returns(data):
    arr = np.diff(np.log(data))
    return (pd.Series(arr, index=data.index[1:]))

time_bar_return = returns(time_bars.close)
tick_bar_return = returns(tick_bars.close)
volume_bar_return = returns(volume_bars.close)
dollar_bar_return = returns(dollar_bars.close)

bar_types = ['time', 'tick','volume','dollar']
bar_returns = [time_bar_return, tick_bar_return, volume_bar_return, dollar_bar_return]

def get_test_stats(bar_types,bar_returns,test_func,*args,**kwds):
    dct = {bar:(int(bar_ret.shape[0]), test_func(bar_ret,*args,**kwds)) for bar,bar_ret in zip(bar_types,bar_returns)}
    result = (pd.DataFrame.from_dict(dct).rename(index={0:'sample_size',1:f'{test_func.__name__}_stat'}).T)
    return result

autocorrs = get_test_stats(bar_types,bar_returns,pd.Series.autocorr)
print(autocorrs.sort_values('autocorr_stat'), autocorrs.abs().sort_values('autocorr_stat'))


def plot_autocorr(bar_types, bar_returns):
    f, axes = plt.subplots(len(bar_types), figsize=(10, 7))

    for i, (bar, typ) in enumerate(zip(bar_returns, bar_types)):
        sm.graphics.tsa.plot_acf(bar, lags=120, ax=axes[i],
                                 alpha=0.05, unbiased=True, fft=True,
                                 zero=False,
                                 title=f'{typ} AutoCorr')
    plt.tight_layout()


def plot_hist(bar_types, bar_rets):
    f, axes = plt.subplots(len(bar_types), figsize=(10, 6))
    for i, (bar, typ) in enumerate(zip(bar_returns, bar_types)):
        g = sns.distplot(bar, ax=axes[i], kde=False, label=typ)
        g.set(yscale='log')
        axes[i].legend()
    plt.tight_layout()


plot_autocorr(bar_types, bar_returns)

plot_hist(bar_types, bar_returns)
def jb(x,test=True):
    np.random.seed(0)
    if test: return stats.jarque_bera(x)[0]
    return stats.jarque_bera(x)[1]

get_test_stats(bar_types,bar_returns,jb).sort_values('jb_stat')
