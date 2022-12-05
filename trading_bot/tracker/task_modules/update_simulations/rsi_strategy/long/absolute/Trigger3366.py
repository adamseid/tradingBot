from re import I

from sympy import N
from .....misc import Misc
import pandas as pd
import time
import os

INITIAL_BALANCE = [1000]
CASH_ALLOCATION = [1]
trials = ['2022-11-8.csv']

def update(symbol):
    Misc.printDebug('Trigger3366.update(): STARTED')


    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')



    new_time = time.time()
    new_price = new_data['close'][len(new_data)-1]
    new_rsi = new_data['rsi'][len(new_data)-1]


    for i in range(len(trials)):
        trial = trials[i]
        print(trial)

        try:
            simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66/' + symbol + '/' + trial)
        except:
            print('NO SYMBOL: ' + symbol)
            Misc.printDebug('Trigger3366.update(): FINISHED')
            return 0

        if str(simulation['time'][len(simulation)-1]) == 'x':
            print('initial run')

            simulation['time'][len(simulation)-1] = new_time
            simulation['price'][len(simulation)-1] = new_price
            simulation['rsi'][len(simulation)-1] = new_rsi
            simulation['cash_allocation'][len(simulation)-1] = CASH_ALLOCATION[i]
            simulation['coin_allocation'][len(simulation)-1] = 1 - CASH_ALLOCATION[i]
            simulation['cash_balance'][len(simulation)-1] = CASH_ALLOCATION[i] * INITIAL_BALANCE[i]
            simulation['coin_balance'][len(simulation)-1] = ((1 - CASH_ALLOCATION[i]) * INITIAL_BALANCE[i]) / new_price
            simulation['total_balance'][len(simulation)-1] = simulation['cash_balance'][len(simulation)-1] + simulation['coin_balance'][len(simulation)-1]
            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66/' + symbol + '/' + trial, index=False)





        else:
            print('not initial run')

            change_price = new_price - simulation['price'][len(simulation)-1]

            coin_allocation = simulation['coin_allocation'][len(simulation)-1]
            cash_allocation = simulation['cash_allocation'][len(simulation)-1]

            coin_balance = simulation['coin_balance'][len(simulation)-1]
            cash_balance = simulation['cash_balance'][len(simulation)-1]

            if new_rsi < 33:
                print('new_rsi < 33')
                if cash_allocation == 1:
                    print('cash_allocation == 1')
                    coin_allocation = 1
                    cash_allocation = 0
                    coin_balance = simulation['cash_balance'][len(simulation)-1] / new_price
                    cash_balance = 0
                else:
                    print('cash_allocation != 1')
                    pass

            elif new_rsi >= 33 and new_rsi < 66:
                print('new_rsi >= 33 and new_rsi < 66')
                pass

            else:
                print('new_rsi >=66')
                if cash_allocation == 1:
                    print('cash_allocation == 1')
                    pass
                else:
                    print('cash_allocation != 1')
                    coin_allocation = 0
                    cash_allocation = 1
                    cash_balance = new_price*simulation['coin_balance'][len(simulation)-1]
                    coin_balance = 0


            total_balance = cash_balance + new_price*coin_balance
            profit = total_balance - simulation['total_balance'][len(simulation)-1]
            total_profit = 0

            simulation.loc[len(simulation)] = [
                new_time,
                new_price,
                change_price,
                new_rsi,
                coin_allocation,
                cash_allocation,
                coin_balance,
                cash_balance,
                total_balance,
                profit,
                total_profit,

            ]

            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66/' + symbol + '/' + trial, index=False)




    Misc.printDebug('Trigger3366.update(): FINISHED')


