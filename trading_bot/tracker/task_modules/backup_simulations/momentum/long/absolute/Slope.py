from .....misc import Misc
import pandas as pd
import time
import os

#trials = ['2022-11-10']

def backup(symbol):
    Misc.printDebug('Slope.backup(): STARTED')

    try:
        trials = os.listdir('../storage/crypto/BINANCE/tables/current/simulations/momentum/long/absolute/slope/' + symbol)
    except:
        print('SYMBOL NOT FOUND: ' + symbol)
        Misc.printDebug('Slope.backup(): FINISHED')
        return 0


    for i in range(len(trials)):
        trial = trials[i]
        trial = os.path.splitext(trial)
        trial = trial[0]
        print(trial)
        simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/momentum/long/absolute/slope/' + symbol + '/' + trial + '.csv')
        #print(simulation)
        #print(os.listdir('../storage/crypto/BINANCE/tables/backup/simulations/macd/long'))
        simulation.to_csv('../storage/crypto/BINANCE/tables/backup/simulations/momentum/long/absolute/slope/' + symbol + '/' + trial + '/' + str(time.time()) + '.csv', index=False)

    Misc.printDebug('Slope.backup(): FINISHED')

