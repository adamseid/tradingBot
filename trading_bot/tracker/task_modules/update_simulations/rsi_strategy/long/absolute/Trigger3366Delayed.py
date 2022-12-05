from re import I

from sympy import N
from .....misc import Misc
import pandas as pd
import time
import os

INITIAL_BALANCE = [1000]
CASH_ALLOCATION = [1]
state = 'wait'

def logic(state, new_price, simulation):
    Misc.printDebug('Trigger3366Delayed.logic(): STARTED')
    cash_allocation = 1

    if state == 'wait':
        print('state == wait')
        cash_allocation = 1
        coin_balance = simulation['Cash Balance'][len(simulation)-1] / new_price
        cash_balance = 0

    elif state == 'prepare-buy':
        print('state == prepare-buy')
        cash_allocation = 1

    elif state == 'hold':
        print('state == hold')
        state = 'prepare-buy'
        cash_allocation = 0

    #not possible
    elif state == 'prepare-sell':
        print('state == prepare-sell')
        cash_allocation = 0

    #not possible
    else: 
        pass

    coin_allocation = 1 - cash_allocation

    Misc.printDebug('Trigger3366Delayed.logic(): FINISHED')
    return cash_allocation, coin_allocation



def update(symbol):
    Misc.printDebug('Trigger3366Delayed.update(): STARTED')


    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')



    new_time = time.time()
    new_price = new_data['close'][len(new_data)-1]
    new_rsi = new_data['rsi'][len(new_data)-1]


    try:
        trials = os.listdir('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66_delayed/' + symbol + '/')
        print(trials)
    except:
        print('NO SYMBOL: ' + symbol)
        Misc.printDebug('Trigger3366Delayed.update(): FINISHED')
        return 0

    for i in range(len(trials)):
        trial = trials[i]
        print(trial)


        simulation = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66_delayed/' + symbol + '/' + trial)


        if str(simulation['Time'][len(simulation)-1]) == 'x':
            print('initial run')

            simulation['Time'][len(simulation)-1] = new_time
            simulation['Price'][len(simulation)-1] = new_price
            simulation['Price Change'][len(simulation)-1] = 0
            simulation['RSI'][len(simulation)-1] = new_rsi
            simulation['State'][len(simulation)-1] = -2
            simulation['Cash Allocation'][len(simulation)-1] = CASH_ALLOCATION[i]
            simulation['Coin Allocation'][len(simulation)-1] = 1 - CASH_ALLOCATION[i]
            simulation['Cash Balance'][len(simulation)-1] = CASH_ALLOCATION[i] * INITIAL_BALANCE[i]
            simulation['Coin Balance'][len(simulation)-1] = ((1 - CASH_ALLOCATION[i]) * INITIAL_BALANCE[i]) / new_price
            simulation['Value'][len(simulation)-1] = simulation['Cash Balance'][len(simulation)-1] + simulation['Coin Balance'][len(simulation)-1]
            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66_delayed/' + symbol + '/' + trial, index=False)





        else:
            print('not initial run')

            state = simulation['State'][len(simulation)-1]
            change_price = new_price - simulation['Price'][len(simulation)-1]

            coin_allocation = simulation['Coin Allocation'][len(simulation)-1]
            cash_allocation = simulation['Cash Allocation'][len(simulation)-1]

            coin_balance = simulation['Coin Balance'][len(simulation)-1]
            cash_balance = simulation['Cash Balance'][len(simulation)-1]

            if new_rsi < 33:
                print('new_rsi < 33')

                #state ==  wait
                if state == -2:
                    print('state == wait')
                    state = -1#'prepare-buy'

                #state == prepare-buy
                elif state == -1:
                    print('state == prepare-buy')
                    pass

                #sell
                #state == hold
                elif state == 2:
                    print('state == hold')
                    pass #instead of sell, stay hold
                    #state = -1#'prepare-buy'
                    #coin_allocation = 0
                    #cash_allocation = 1
                    #cash_balance = new_price*simulation['Coin Balance'][len(simulation)-1]
                    #coin_balance = 0

                #not possible
                #state == prepare-sell
                elif state == 1:
                    print('state == prepare-sell')
                    pass

                #not possible
                else: 
                    pass


                '''
                if cash_allocation == 1:
                    print('cash_allocation == 1')
                    coin_allocation = 1
                    cash_allocation = 0
                    coin_balance = simulation['cash_balance'][len(simulation)-1] / new_price
                    cash_balance = 0

                else:
                    print('cash_allocation != 1')
                    pass

                '''

            elif new_rsi >= 33 and new_rsi < 66:
                print('new_rsi >= 33 and new_rsi < 66')

                #state ==  wait
                if state == -2:
                    print('state == wait')
                    pass

                #buy
                #prepare-buy
                elif state == -1:
                    print('state == prepare-buy')
                    state = 2#'hold'
                    coin_allocation = 1
                    cash_allocation = 0
                    coin_balance = simulation['Cash Balance'][len(simulation)-1] / new_price
                    cash_balance = 0

                #state == hold
                elif state == 2:
                    print('state == hold')
                    pass

                #sell
                #state == prepare-sell
                elif state == 1:
                    print('state == prepare-sell')
                    state = -2#'wait'
                    coin_allocation = 0
                    cash_allocation = 1
                    cash_balance = new_price*simulation['Coin Balance'][len(simulation)-1]
                    coin_balance = 0

                #not possible
                else:
                    pass


            elif new_rsi >= 66:
                print('new_rsi >=66')

                #buy
                #state ==  wait
                if state == -2:
                    print('state == wait')
                    pass #instead of buy, wait
                    #state = 1#'prepare-sell'
                    #coin_allocation = 1
                    #cash_allocation = 0
                    #coin_balance = simulation['Cash Balance'][len(simulation)-1] / new_price
                    #cash_balance = 0

                #not possible
                #state == prepare-buy
                elif state == -1:
                    print('state == prepare-buy')
                    pass

                #state == hold
                elif state == 2:
                    print('state == hold')
                    state = 1#'prepare-sell'

                #state == prepare-sell
                elif state == 1:
                    print('state == prepare-sell')
                    pass


                '''
                if cash_allocation == 1:
                    print('cash_allocation == 1')
                    pass
                else:
                    print('cash_allocation != 1')
                    coin_allocation = 0
                    cash_allocation = 1
                    cash_balance = new_price*simulation['coin_balance'][len(simulation)-1]
                    coin_balance = 0
                '''
            #not possible
            else:
                pass


            

            value = cash_balance + new_price*coin_balance


            simulation.loc[len(simulation)] = [
                new_time,
                new_price,
                change_price,
                new_rsi,
                state,
                cash_allocation,
                coin_allocation,
                cash_balance,
                coin_balance,
                value
            ]

            simulation.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/long/absolute/trigger_33_66_delayed/' + symbol + '/' + trial, index=False)




    Misc.printDebug('Trigger3366Delayed.update(): FINISHED')


