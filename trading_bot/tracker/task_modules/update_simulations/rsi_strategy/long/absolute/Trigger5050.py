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
    Misc.printDebug('Trigger5050.update(): STARTED')
    print(symbol)

    #print(os.listdir('../storage/crypto/BINANCE/tables/current/raw/'))
    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')
    #print(new_data)

    new_time = time.time()
    new_price = new_data['close'][len(new_data)-1]
    new_rsi = new_data['rsi'][len(new_data)-1]

    #print(new_time, new_price, new_rsi)

    for i in range(len(trials)):
        trial = trials[i]
        print(trial)

        try:
            simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_50_50/' + symbol + '/' + trial)
            #print(simulation)
        except:
            print('NO SYMBOL: ' + symbol)
            Misc.printDebug('Trigger5050.update(): FINISHED')
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
            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_50_50/' + symbol + '/' + trial, index=False)


            #print(simulation)



        else:
            print('not initial run')

            change_price = new_price - simulation['price'][len(simulation)-1]

            coin_allocation = simulation['coin_allocation'][len(simulation)-1]
            cash_allocation = simulation['cash_allocation'][len(simulation)-1]

            #print(cash_allocation)
            coin_balance = simulation['coin_balance'][len(simulation)-1]
            cash_balance = simulation['cash_balance'][len(simulation)-1]

            if new_rsi < 50:
                print('new_rsi <50')
                if cash_allocation == 1:
                    print('cash_allocation == 1')
                    coin_allocation = 1
                    cash_allocation = 0
                    coin_balance = simulation['cash_balance'][len(simulation)-1] / new_price
                    cash_balance = 0
                else:
                    print('cash_allocation != 1')
                    pass



            else:
                print('new_rsi >=50')
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

            #print(simulation)
            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_50_50/' + symbol + '/' + trial, index=False)




    Misc.printDebug('Trigger5050.update(): FINISHED')


