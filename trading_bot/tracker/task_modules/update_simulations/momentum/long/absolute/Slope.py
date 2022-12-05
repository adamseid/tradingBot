from re import I

from sympy import N
from .....misc import Misc
import pandas as pd
import time
import os

INITIAL_BALANCE = [1000]
CASH_ALLOCATION = [1]
#trials = ['2022-11-10.csv']


def logic(new_price, momentum_change, cash_allocation, coin_allocation, cash_balance, coin_balance, simulation):
    Misc.printDebug('Slope.logic(): STARTED')


    if momentum_change < 0:
        print('momentum_change < 0')
        if cash_allocation == 1:
            print('cash_allocation == 1')
            pass

        else:
            print('cash_allocation != 1')
            coin_allocation = 0
            cash_allocation = 1
            cash_balance = new_price*simulation['Coin Balance'][len(simulation)-1]
            coin_balance = 0
            

    elif momentum_change == 0:
        print('momentum_change == 0')
        pass

    else:
        print('momentum_change > 0')
        if cash_allocation == 1:
            print('cash_allocation == 1')
            coin_allocation = 1
            cash_allocation = 0
            coin_balance = simulation['Cash Balance'][len(simulation)-1] / new_price
            cash_balance = 0
        else:
            print('cash_allocation != 1')
            pass





    Misc.printDebug('Slope.logic(): FINISHED')
    return cash_allocation, coin_allocation, cash_balance, coin_balance


def update(symbol):
    Misc.printDebug('Slope.update(): STARTED')
    
    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')
    new_time = time.time()
    new_price = new_data['close'][len(new_data)-1]
    new_momentum = new_data['mom'][len(new_data)-1]

    try:
        trials = os.listdir('../storage/crypto/BINANCE/tables/current/simulations/momentum/long/absolute/slope/' + symbol + '/')
        print(trials)
    except:
        print('NO SYMBOL: ' + symbol)
        Misc.printDebug('Slope.update(): FINISHED')
        return 0

    for i in range(len(trials)):
        trial = trials[i]
        print(trial)
        simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/momentum/long/absolute/slope/' + symbol + '/' + trial)
        if str(simulation['Time'][len(simulation)-1]) == 'x':
            print('initial run')
            simulation['Time'][len(simulation)-1] = new_time
            simulation['Price'][len(simulation)-1] = new_price
            simulation['Price Change'][len(simulation)-1] = 0
            simulation['Momentum'][len(simulation)-1] = new_momentum
            simulation['Momentum Change'][len(simulation)-1] = 0
            simulation['Cash Allocation'][len(simulation)-1] = CASH_ALLOCATION[i]
            simulation['Coin Allocation'][len(simulation)-1] = 1 - CASH_ALLOCATION[i]
            simulation['Cash Balance'][len(simulation)-1] = CASH_ALLOCATION[i] * INITIAL_BALANCE[i]
            simulation['Coin Balance'][len(simulation)-1] = ((1 - CASH_ALLOCATION[i]) * INITIAL_BALANCE[i]) / new_price
            simulation['Total Balance'][len(simulation)-1] = simulation['Cash Balance'][len(simulation)-1] + simulation['Coin Balance'][len(simulation)-1]
            print(simulation)
            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/momentum/long/absolute/slope/' + symbol + '/' + trial, index=False)
         
        else:
            print('not initial run')
            
            price_change = new_price - simulation['Price'][len(simulation)-1]
            momentum_change = new_momentum - simulation['Momentum'][len(simulation)-1]

            cash_allocation = simulation['Cash Allocation'][len(simulation)-1]
            coin_allocation = simulation['Coin Allocation'][len(simulation)-1]

            cash_balance = simulation['Cash Balance'][len(simulation)-1]
            coin_balance = simulation['Coin Balance'][len(simulation)-1]

            cash_allocation, coin_allocation, cash_balance, coin_balance = logic(new_price, momentum_change, cash_allocation, coin_allocation, cash_balance, coin_balance, simulation)
            total_balance = cash_balance + new_price*coin_balance

            simulation.loc[len(simulation)] = [
                new_time,
                new_price,
                price_change,
                new_momentum,
                momentum_change,
                cash_allocation,
                coin_allocation,
                cash_balance,
                coin_balance,
                total_balance,
            ]

            #print(simulation)
            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/momentum/long/absolute/slope/' + symbol + '/' + trial, index=False)
           
    Misc.printDebug('Slope.update(): FINISHED')


