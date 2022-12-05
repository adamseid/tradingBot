from .....misc import Misc
from .dprice_average_1m import ddPrice


import pandas as pd
import numpy as np

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_5m/dprice/dprice_average_1m.csv'
RAW_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_5m/dprice.csv'


def updateSelf(symbols):
    Misc.printDebug('dPriceAverage1m.updateSelf(): STARTED')
    raw = pd.read_csv(RAW_PATH)
    try:
        df = pd.read_csv(CSV_PATH)
    except:
        df = pd.DataFrame(columns=list(raw.head()))
    df.loc[len(df.index)] = list(np.zeros(df.shape[1]))
    for symbol in list(raw.head()):
        if symbol == 'time':
            df['time'][len(df)-1] = raw['time'][len(raw)-1]
        else:
            # Compute Average
            df[symbol][len(df)-1] = raw[symbol][len(raw)-1]
    df.to_csv(CSV_PATH, index=False)
    Misc.printDebug('dPriceAverage1m.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('dPriceAverage1m.update(): STARTED')

    updateSelf(symbols)
    ddPrice.update(symbols)

    Misc.printDebug('dPriceAverage1m.update(): FINISHED')


