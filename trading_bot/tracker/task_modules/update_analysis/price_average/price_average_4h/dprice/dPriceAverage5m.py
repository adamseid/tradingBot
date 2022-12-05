from .....misc import Misc
import pandas as pd
import numpy as np
from .dprice_average_5m import ddPrice

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_4h/dprice/dprice_average_5m.csv'
RAW_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_4h/dprice.csv'
dt = 5

def updateSelf(symbols):
    Misc.printDebug('dPriceAverage5m.updateSelf(): STARTED')
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
            if len(raw) > dt:
                df[symbol][len(df)-1] = np.mean(np.array(raw.tail(dt)[symbol]))
                print('compute average')
            else:
                df[symbol][len(df)-1] = raw[symbol][len(raw)-1]
                print('not enough for average')
    df.to_csv(CSV_PATH, index=False)
    #print(df)
    Misc.printDebug('dPriceAverage5m.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('dPriceAverage5m.update(): STARTED')

    updateSelf(symbols)
    ddPrice.update(symbols)

    Misc.printDebug('dPriceAverage5m.update(): FINISHED')
