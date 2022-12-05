
from .....misc import Misc
import os
import pandas as pd
import time
from .over_under import Difference30m

#STILL HAVE TO CREATE COIN NAME IN DIRECTORY LIKE: BTCUSDT, ETHUSDT, etc...

INITIAL_VALUE = 1000
INITIAL_CASH_ALLOCATION = 1

def path(symbol):
    return '../storage/crypto/BINANCE/tables/current/simulations/moving_average/long/absolute/over_under/' + symbol + '/'

def updateAnalysis(symbol):
    #at this point a new row in raw is already created
    raw = pd.read_csv(path(symbol) + 'raw.csv')
    print(raw)
    analysis = pd.read_csv(path(symbol) + 'analysis.csv')
    

    time = raw['Time'][len(raw)-1]
    price_1m = raw['Price'][len(raw)-1]

    change_1m = raw['Price'][len(raw)-1] - raw['Price'][len(raw)-2]
    change_5m = raw['Average Price 5m'][len(raw)-1] - raw['Average Price 5m'][len(raw)-2]
    change_30m = raw['Average Price 30m'][len(raw)-1] - raw['Average Price 30m'][len(raw)-2]
    change_4h = raw['Average Price 4h'][len(raw)-1] - raw['Average Price 4h'][len(raw)-2]
    rate_1m = change_1m/(time - raw['Time'][len(raw)-2]) * 60 # $/minute
    rate_5m = change_5m/(time - raw['Time'][len(raw)-2]) * 60
    rate_30m = change_30m/(time - raw['Time'][len(raw)-2]) * 60
    rate_4h = change_4h/(time - raw['Time'][len(raw)-2]) * 60
    difference_5m = raw['Price'][len(raw)-1] - raw['Average Price 5m'][len(raw)-1]
    difference_30m = raw['Price'][len(raw)-1] - raw['Average Price 30m'][len(raw)-1]
    difference_4h = raw['Price'][len(raw)-1] - raw['Average Price 4h'][len(raw)-1]


    analysis.loc[len(analysis)] = [
        int(time),
        round(price_1m, 4),
        round(change_1m, 4),
        round(change_5m, 4),
        round(change_30m, 4),
        round(change_4h, 4),
        round(rate_1m, 4),
        round(rate_5m, 4),
        round(rate_30m, 4),
        round(rate_4h, 4),
        round(difference_5m, 4),
        round(difference_30m, 4),
        round(difference_4h, 4)
    ]

    print(analysis)
    analysis.to_csv(path(symbol) + 'analysis.csv', index=False)

def update(symbol):
    Misc.printDebug('OverUnder.update(): STARTED')

    new_data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')

    new_time = int(time.time())
    new_price = new_data['close'][len(new_data)-1]
    
    try:
        trials = os.listdir(path(symbol))
        print('FOUND: ' + symbol)
        
    except:
        print('NO SYMBOL: ' + symbol)
        Misc.printDebug('OverUnder.update(): FINISHED')
        return 0

    # Update Raw Data
    simulation = pd.read_csv(path(symbol) + 'raw.csv')
    #print(simulation)

    if str(simulation['Time'][len(simulation)-1]) == 'x':
        print('initial run')
        

        simulation['Time'][len(simulation)-1] = new_time
        simulation['Price'][len(simulation)-1] = new_price
        simulation['Average Price 5m'][len(simulation)-1] = new_price
        simulation['Average Price 30m'][len(simulation)-1] = new_price
        simulation['Average Price 4h'][len(simulation)-1] = new_price
        simulation['Cash Allocation'][len(simulation)-1] = INITIAL_CASH_ALLOCATION
        simulation['Coin Allocation'][len(simulation)-1] = 1 - INITIAL_CASH_ALLOCATION
        simulation['Cash Balance'][len(simulation)-1] = INITIAL_CASH_ALLOCATION * INITIAL_VALUE
        simulation['Coin Balance'][len(simulation)-1] = ((1 - INITIAL_CASH_ALLOCATION) * INITIAL_VALUE) / new_price
        simulation['Value'][len(simulation)-1] = simulation['Cash Balance'][len(simulation)-1] + new_price*simulation['Coin Balance'][len(simulation)-1]


        print(simulation)
        simulation.to_csv(path(symbol) + 'raw.csv', index=False)

    else:
        print('not initial run')


        #setup previous states
        cash_allocation = simulation['Cash Allocation'][len(simulation)-1]
        coin_allocation = simulation['Coin Allocation'][len(simulation)-1]
        cash_balance = simulation['Cash Balance'][len(simulation)-1]
        coin_balance = simulation['Coin Balance'][len(simulation)-1]
        
        if len(simulation) < 5:
            print('len(simulation) < 5')
            average_price_5m = new_price
            average_price_30m = new_price
            average_price_4h = new_price
        elif len(simulation) < 30:
            print('len(simulation) < 30')
            average_price_5m = simulation['Price'].tail(5).mean()
            average_price_30m = new_price
            average_price_4h = new_price
        elif len(simulation) < 240:
            print('len(simulation) < 240')
            average_price_5m = simulation['Price'].tail(5).mean()
            average_price_30m = simulation['Price'].tail(30).mean()
            average_price_4h = new_price
        else:
            average_price_5m = simulation['Price'].tail(5).mean()
            average_price_30m = simulation['Price'].tail(30).mean()
            average_price_4h = simulation['Price'].tail(240).mean()

        price_difference = new_price - average_price_5m

        value = cash_balance + new_price*coin_balance


        simulation.loc[len(simulation)] = [
            new_time,
            round(new_price, 4),
            round(average_price_5m, 4),
            round(average_price_30m, 4),
            round(average_price_4h, 4),
            round(cash_allocation, 4),
            round(coin_allocation, 4),
            round(cash_balance, 4),
            round(coin_balance, 4),
            round(value, 2)
        ]
        #print(simulation)
        simulation.to_csv(path(symbol) + 'raw.csv', index=False)



    # Update Analysis Data
    updateAnalysis(symbol)

    # Update Portfolios
    Difference30m.update(symbol)



    Misc.printDebug('OverUnder.update(): FINISHED')


