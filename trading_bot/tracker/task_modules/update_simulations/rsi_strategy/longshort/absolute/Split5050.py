from .....misc import Misc
import pandas as pd
import os
import time


def update(symbol):
    Misc.printDebug('Split5050.update(): STARTED')
    print(symbol)

    #print(os.listdir('../storage/crypto/BINANCE/tables/current/raw/'))
    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')
    #print(new_data)

    new_time = time.time()
    new_price = new_data['close'][len(new_data)-1]
    new_rsi = new_data['rsi'][len(new_data)-1]

    #print(new_time, new_price, new_rsi)

    simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/longshort/absolute/split5050/' + symbol + '/2022-10-24.csv')
    #print(simulation)


    Misc.printDebug('Split5050.update(): FINISHED')

