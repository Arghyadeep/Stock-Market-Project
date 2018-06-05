#dependencies
import pandas as pd
from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as datetime
import numpy as np
from stockstats import StockDataFrame as sdf
import sys
import matplotlib.cm as cm

def read_file(filename):
    path = "data/"
    try:
        data = pd.read_csv(path+filename)
        data.dropna(inplace=True,axis = 0)
        return data
    except:
        print ("File does not exist")
        sys.exit()

def get_intraday_values(data):
    Open = list(data['Open'][1:])
    High = list(data['High'][1:])
    Low = list(data['Low'][1:])
    Close = list(data['Close'][1:])
    return Open, High, Low, Close


def create_outputs(data):
    Open = list(data['Open'])
    Close = list(data['Close'])
    Y = []
    for i in range(len(Open)):
        change = (Close[i]-Open[i])/Open[i]*100
        Y.append(change)
    return Y
    

def create_dataframe(data,outputs):
    stock = sdf.retype(data)
    stock['macd']
    stock['macds']
    stock['rsi_12']
    stock['rsi_6']
    stock['boll']
    stock['boll_ub']
    stock['boll_lb']
    stock['cci_20']
    stock['cci_14']
    stock['atr']
    stock['tr']
    stock['vr']
    stock['Y'] = Y
    del stock['open']
    del stock['high']
    del stock['low']
    del stock['close']
    del stock['adj close']
    del stock['volume']
    del stock['close_-1_s']
    del stock['close_-1_d']
    del stock['rs_12']
    del stock['rs_6']
    del stock['middle']
    del stock['change']
    del stock['macdh']
    del stock['close_20_sma']
    del stock['close_20_mstd']
    del stock['boll']
    stock.dropna(inplace= True,axis = 0)
    stock.drop(stock.index[[0]]) #needs to be fixed in order to remove all inf values
    print(stock.info())
    return stock

def plot_tech_indicators(Open, high, Low, Close, tech_data, indicators):
    fig,ax = plt.subplots()
    candlestick2_ohlc(ax, Open, High, Low, Close, width=0.6)
    #create a general color scheme
    colors = ['r','g','b','y','v']
    col = 0
    for indicator in indicators:
        plt.plot(list(tech_data[indicator]), colors[col])
        col += 1
    #add legend
    plt.show()
    #save plot to a new folder

filename = 'AAPL.csv'
data = read_file(filename)
Open, High, Low, Close = get_intraday_values(data)
Y = create_outputs(data)
stock = create_dataframe(data,Y)
plot_tech_indicators(Open, High, Low, Close, stock, ['boll_ub','boll_lb','close_12_ema','close_26_ema'])
print(len(Open))
