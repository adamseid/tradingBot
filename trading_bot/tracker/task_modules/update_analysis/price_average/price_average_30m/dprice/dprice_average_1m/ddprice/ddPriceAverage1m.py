from .......misc import Misc
import pandas as pd
import numpy as np

CSV_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_30m/dprice/dprice_average_1m/ddprice/ddprice_average_1m.csv'
RAW_PATH = '../storage/crypto/BINANCE/tables/current/analysis/price_average/price_average_30m/dprice/dprice_average_1m/ddprice.csv'

def updateSelf(symbols):
    Misc.printDebug('ddPriceAverage1m.updateSelf(): STARTED')
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
    #print(df)
    Misc.printDebug('ddPriceAverage1m.updateSelf(): FINISHED')

def update(symbols):
    Misc.printDebug('ddPriceAverage1m.update(): STARTED')

    updateSelf(symbols)

    Misc.printDebug('ddPriceAverage1m.update(): FINISHED')
