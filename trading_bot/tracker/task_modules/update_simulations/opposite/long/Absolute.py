
from ....misc import Misc
import pandas as pd
import os

def path(symbol):
    return '../storage/crypto/BINANCE/tables/current/simulations/opposite/' + symbol + '/'

def updateRaw(symbol):
    Misc.printDebug('Absolute.updateRaw(): STARTED')
    raw = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')
    portfolio_raw = pd.read_csv(path(symbol) + 'raw.csv')

    time = raw['time'][len(raw)-1]
    price = raw['close'][len(raw)-1]



    if str(portfolio_raw['Time'][len(portfolio_raw)-1]) == 'x':
        print('INITIAL RUN')
        portfolio_raw['Time'][len(portfolio_raw)-1] = int(time)
        portfolio_raw['Price'][len(portfolio_raw)-1] = round(price, 4)
        portfolio_raw['Change'][len(portfolio_raw)-1] = 0
        portfolio_raw['Cash Allocation'][len(portfolio_raw)-1] = 1
        portfolio_raw['Coin Allocation'][len(portfolio_raw)-1] = 0
        portfolio_raw['Cash Balance'][len(portfolio_raw)-1] = 1000
        portfolio_raw['Coin Balance'][len(portfolio_raw)-1] = 0
        portfolio_raw['Value'][len(portfolio_raw)-1] = 1000

        print(portfolio_raw)


    else:
        print('NOT INITIAL RUN')

        cash_allocation = portfolio_raw['Cash Allocation'][len(portfolio_raw)-1]
        coin_allocation = portfolio_raw['Coin Allocation'][len(portfolio_raw)-1]
        cash_balance = portfolio_raw['Cash Balance'][len(portfolio_raw)-1]
        coin_balance = portfolio_raw['Coin Balance'][len(portfolio_raw)-1]

        change = price - raw['close'][len(raw)-2]

        if change > 0:
            print('change > 0')
            if cash_allocation == 1:
                print('cash_allocation == 1')
                pass
            else:
                print('cash_allocation == 0')
                cash_allocation = 1
                coin_allocation = 0
                cash_balance = price*coin_balance
                coin_balance = 0

        elif change == 0:
            print('change == 0')

        else:
            print('change < 0')
            if cash_allocation == 1:
                print('cash_allocation == 1')
                cash_allocation = 0
                coin_allocation = 1
                coin_balance = cash_balance/price
                cash_balance = 0
            else:
                print('cash_allocation == 0')
                pass

            


        value = price*coin_balance + cash_balance
        


        portfolio_raw.loc[len(raw)] = [
            time,
            price,
            change,
            cash_allocation,
            coin_allocation,
            cash_balance,
            coin_balance,
            value
        ]

        print(portfolio_raw)
        
    portfolio_raw.to_csv(path(symbol) + 'raw.csv', index=False)


    Misc.printDebug('Abssolute.updateRaw(): FINISHED')


def update(symbol):
    Misc.printDebug('Absolute.update(): STARTED')

    try:
        trials = os.listdir(path(symbol))
        print('FOUND: ' + symbol)
        
    except:
        print('NO SYMBOL: ' + symbol)
        Misc.printDebug('OverUnder.update(): FINISHED')
        return 0

    updateRaw(symbol)
    Misc.printDebug('Absolute.update(): FINISHED')

