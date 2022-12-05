import numpy as np
import pandas as pd

from ....misc import Misc
from .dprice import dPriceAverage1m

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_1m/dprice.csv'
RAW_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_1m.csv'

def updateSelf(symbols):
    Misc.printDebug('dPrice1m.updateSelf(): STARTED')
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
            df[symbol][len(df)-1] = (raw[symbol][len(raw)-1] - raw[symbol][len(raw)-2])/(raw['time'][len(raw)-1] - raw['time'][len(raw)-2])
    df.to_csv(CSV_PATH, index=False)
    Misc.printDebug('dPrice1m.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('dPrice1m.update(): STARTED')
    updateSelf(symbols)
    dPriceAverage1m.update(symbols)
    Misc.printDebug('dPrice1m.update(): FINISHED')



