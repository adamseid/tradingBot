import numpy as np
import pandas as pd

from ....misc import Misc
from .dprice import dPriceAverage1m, dPriceAverage5m, dPriceAverage30m, dPriceAverage4h

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_30m/dprice.csv'
RAW_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_30m.csv'

INTERVAL = 60 #seconds between each reading

def updateSelf(symbols):
    Misc.printDebug('dPrice.updateSelf(): STARTED')
    raw = pd.read_csv(RAW_PATH)
    try:
        df = pd.read_csv(CSV_PATH)
    except:
        print('except')
        df = pd.DataFrame(columns=list(raw.head()))
    df.loc[len(df.index)] = list(np.zeros(df.shape[1]))
    for symbol in list(raw.head()):
        if symbol == 'time':
            df['time'][len(df)-1] = raw['time'][len(raw)-1]
        else:
            # Compute Derivative
            df[symbol][len(df)-1] = INTERVAL*(raw[symbol][len(raw)-1] - raw[symbol][len(raw)-2])/(raw['time'][len(raw)-1] - raw['time'][len(raw)-2])
    df.to_csv(CSV_PATH, index=False)
    Misc.printDebug('dPrice.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('dPrice.update(): STARTED')
    updateSelf(symbols)
    dPriceAverage1m.update(symbols)
    dPriceAverage5m.update(symbols)
    dPriceAverage30m.update(symbols)
    dPriceAverage4h.update(symbols)

    Misc.printDebug('dPrice.update(): FINISHED')
