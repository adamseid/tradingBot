from .....misc import Misc
import pandas as pd
import time
import os

#trials = ['2022-11-8']

def backup(symbol):
    Misc.printDebug('Trigger5050.backup(): STARTED')

    try:
        trials = os.listdir('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_50_50/' + symbol)
    except:
        print('SYMBOL NOT FOUND: ' + symbol)
        Misc.printDebug('Trigger5050.backup(): FINISHED')
        return 0


    for i in range(len(trials)):
        trial = trials[i]
        trial = trials[i]
        trial = os.path.splitext(trial)
        trial = trial[0]
        print(trial)
        simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_50_50/' + symbol + '/' + trial + '.csv')
        print(simulation)
        simulation.to_csv('../storage/crypto/BINANCE/tables/backup/simulations/rsi/long/absolute/trigger_50_50/' + symbol + '/' + trial + '/' + str(time.time()) + '.csv', index=False)

    Misc.printDebug('Trigger5050.backup(): FINISHED')

