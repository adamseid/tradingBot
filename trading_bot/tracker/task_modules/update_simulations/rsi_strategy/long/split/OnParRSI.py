
from .....misc import Misc
import os
import pandas as pd
import time

#STILL HAVE TO CREATE COIN NAME IN DIRECTORY LIKE: BTCUSDT, ETHUSDT, etc...

INITIAL_VALUE = 1000
INITIAL_CASH_ALLOCATION = 0.5

def path(symbol):
    return '../storage/crypto/BINANCE/tables/current/simulations/rsi/long/split/on_par_rsi/' + symbol + '/'



def update(symbol):
    Misc.printDebug('OnParRSI.update(): STARTED')

    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')

    new_time = int(time.time())
    new_price = new_data['close'][len(new_data)-1]
    new_rsi = new_data['rsi'][len(new_data)-1]
    
    try:
        trials = os.listdir(path(symbol))
        print('FOUND: ' + symbol)
        
    except:
        print('NO SYMBOL: ' + symbol)
        Misc.printDebug('OnParRSI.update(): FINISHED')
        return 0

    for i in range(len(trials)):
        trial = trials[i]
        print(trial)

        simulation = pd.read_csv(path(symbol) + trial)
        #print(simulation)

        if str(simulation['Time'][len(simulation)-1]) == 'x':
            print('initial run')
            

            simulation['Time'][len(simulation)-1] = new_time
            simulation['Price'][len(simulation)-1] = new_price
            simulation['RSI'][len(simulation)-1] = new_rsi
            simulation['Cash Allocation'][len(simulation)-1] = INITIAL_CASH_ALLOCATION
            simulation['Coin Allocation'][len(simulation)-1] = 1 - INITIAL_CASH_ALLOCATION
            simulation['Cash Balance'][len(simulation)-1] = INITIAL_CASH_ALLOCATION * INITIAL_VALUE
            simulation['Coin Balance'][len(simulation)-1] = ((1 - INITIAL_CASH_ALLOCATION) * INITIAL_VALUE) / new_price
            simulation['Value'][len(simulation)-1] = simulation['Cash Balance'][len(simulation)-1] + new_price*simulation['Coin Balance'][len(simulation)-1]


            print(simulation)
            simulation.to_csv(path(symbol) + trial, index=False)

        else:
            print('not initial run')

            #print(new_rsi/100)
            cash_allocation = new_rsi/100
            coin_allocation = 1 - cash_allocation
            

            #setup previous states
            cash_balance = simulation['Cash Balance'][len(simulation)-1]
            coin_balance = simulation['Coin Balance'][len(simulation)-1]
            
            #operations
            print(cash_balance, coin_balance)
            new_value = cash_balance + new_price*coin_balance
            print('VALUE', simulation['Value'][len(simulation)-1], new_value)

            new_cash_allocation = cash_balance/new_value
            new_coin_allocation = new_price*coin_balance/new_value
            print(new_cash_allocation, new_coin_allocation)

            cash_allocation_change = new_cash_allocation - cash_allocation
            coin_allocation_change = new_coin_allocation - coin_allocation
            print(cash_allocation_change, coin_allocation_change)

            cash_balance_change = cash_allocation_change*new_value
            coin_balance_change = coin_allocation_change*new_value/new_price
            print(cash_balance_change, coin_balance_change)
            
            # MARKET ORDERS
            cash_balance = cash_balance - cash_balance_change
            coin_balance = coin_balance - coin_balance_change
            

            value = new_value


            simulation.loc[len(simulation)] = [
                new_time,
                new_price,
                new_rsi,
                cash_allocation,
                coin_allocation,
                cash_balance,
                coin_balance,
                value
            ]
            #print(simulation)
            simulation.to_csv(path(symbol) + trial, index=False)


    Misc.printDebug('OnParRSI.update(): FINISHED')


