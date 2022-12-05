from ...misc import Misc
from .price_average_5m import dPrice
import pandas as pd
import numpy as np

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_5m.csv'

dt = 5

def rawPath(symbol):
    return '../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv'

def updateSelf(symbols):
    Misc.printDebug('PriceAverage5m.updateSelf(): STARTED')
    df = pd.read_csv(CSV_PATH)
    df.loc[len(df.index)] = list(np.zeros(df.shape[1]))
    for i in range(len(symbols)):
        raw = pd.read_csv(rawPath(symbols[i]))
        df['time'][len(df)-1] = raw['time'][len(raw)-1]
        try:
            # Compute average from last 5 values of raw['close']
            df[symbols[i]][len(df)-1] = np.mean(np.array(raw.tail(dt)['close']))
        except:
            new_column = list(np.zeros(len(df)-1))
            new_column.append(raw['close'][len(raw)-1])
            df = df.join(pd.DataFrame({symbols[i]: new_column}))
    df.to_csv(CSV_PATH, index=False)
    Misc.printDebug('PriceAverage5m.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('PriceAverage5m.update(): STARTED')

    updateSelf(symbols)
    dPrice.update(symbols)

    Misc.printDebug('PriceAverage5m.update(): FINISHED')

