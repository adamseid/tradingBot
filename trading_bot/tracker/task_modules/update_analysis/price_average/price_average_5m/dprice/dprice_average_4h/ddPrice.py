from ......misc import Misc
from .ddprice import ddPriceAverage1m, ddPriceAverage5m, ddPriceAverage30m, ddPriceAverage4h
import pandas as pd
import numpy as np

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_5m/dprice/dprice_average_4h/ddprice.csv'
RAW_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_5m/dprice/dprice_average_4h.csv'
INTERVAL = 60 #seconds between each reading


def updateSelf(symbols):
    Misc.printDebug('ddPrice.updateSelf(): STARTED')
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
    print(df)
    df.to_csv(CSV_PATH, index=False)
    Misc.printDebug('ddPrice.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('ddPrice.update(): STARTED')
    updateSelf(symbols)
    
    ddPriceAverage1m.update(symbols)
    ddPriceAverage5m.update(symbols)
    ddPriceAverage30m.update(symbols)
    ddPriceAverage4h.update(symbols)

    Misc.printDebug('ddPrice.update(): FINISHED')



