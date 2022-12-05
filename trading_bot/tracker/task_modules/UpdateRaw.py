from tradingview_ta import TA_Handler, Interval
import csv
import os
from .misc import Misc
import time
import pandas as pd

def get_ta_data(symbol, screener, exchange, interval):
    Misc.printDebug('UpdateRaw.get_ta_data(): STARTED')
    handler_1m = TA_Handler(symbol=symbol,
        screener=screener,
        exchange=exchange,
        interval = interval
        )
    analysis = handler_1m.get_analysis()
    ta_data = [time.time()]
    ta_data.append(analysis.indicators["open"])
    ta_data.append(analysis.indicators["close"])
    ta_data.append(analysis.indicators["MACD.macd"])
    ta_data.append(analysis.indicators['Mom'])
    ta_data.append(analysis.indicators["RSI"])
    Misc.printDebug('UpdateRaw.get_ta_data(): FINISHED')
    return ta_data

#symbols = ['BTCUPUSDT', 'BTCDOWNUSDT']

def update(symbols):
    Misc.printDebug('UpdateRaw.update(): STARTED')
    screener = 'crypto'
    exchange = 'BINANCE'

    for symbol in symbols:
        print('\n', 'Currently Updating: ' + symbol)
        data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')
        ta_data = get_ta_data(symbol, screener, exchange, Interval.INTERVAL_1_MINUTE)
        print(ta_data)
        data.loc[len(data)] = ta_data
        data.to_csv('../storage/crypto/BINANCE/tables/current/raw/'+ symbol + '.csv', index=False)


    Misc.printDebug('UpdateRaw.update(): FINISHED')


