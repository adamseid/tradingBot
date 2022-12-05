from ......misc import Misc
import pandas as pd

def path(symbol):
    return '../storage/crypto/BINANCE/tables/current/simulations/moving_average/long/absolute/over_under/' + symbol + '/'

def updateRaw(symbol):
    Misc.printDebug('Difference30m().updateRaw(): STARTED')
    analysis = pd.read_csv(path(symbol) + 'analysis.csv')
    portfolio_raw = pd.read_csv(path(symbol) + 'difference_30m/raw.csv')

    time = analysis['Time'][len(analysis)-1]
    price = analysis['Price 1m'][len(analysis)-1]
    difference_30m = analysis['Difference 30m'][len(analysis)-1]

    if str(portfolio_raw['Time'][len(portfolio_raw)-1]) == 'x':
        print('INITIAL RUN')


        portfolio_raw['Time'][len(portfolio_raw)-1] = round(time, 2)
        portfolio_raw['Price'][len(portfolio_raw)-1] = round(price, 2)
        portfolio_raw['Difference 30m'][len(portfolio_raw)-1] = round(difference_30m, 2)
        portfolio_raw['Cash Allocation'][len(portfolio_raw)-1] = 1
        portfolio_raw['Coin Allocation'][len(portfolio_raw)-1] = 0
        portfolio_raw['Cash Balance'][len(portfolio_raw)-1] = 1000
        portfolio_raw['Coin Balance'][len(portfolio_raw)-1] = 0
        portfolio_raw['Value'][len(portfolio_raw)-1] = 1000

        print(portfolio_raw)
        portfolio_raw.to_csv(path(symbol) + '/difference_30m/raw.csv', index=False)



    else:
        print('NOT INITIAL RUN')
        cash_allocation = portfolio_raw['Cash Allocation'][len(portfolio_raw)-1]
        coin_allocation = portfolio_raw['Coin Allocation'][len(portfolio_raw)-1]
        cash_balance = portfolio_raw['Cash Balance'][len(portfolio_raw)-1]
        coin_balance = portfolio_raw['Coin Balance'][len(portfolio_raw)-1]


        if difference_30m > 0:
            print('difference_30m > 0')
            if cash_allocation == 1:
                print('cash_allocation == 1')
                cash_allocation = 0
                coin_allocation = 1
                coin_balance = cash_balance/price
                cash_balance = 0
            else:
                print('cash_allocation == 0')
                cash_allocation = 0
                coin_allocation = 1

        elif difference_30m == 0:
            pass

        else:
            print('difference_30 < 0')
            if cash_allocation == 1:
                print('cash_allocation == 1')
                cash_allocation = 1
                coin_allocation = 0
            else:
                print('cash_allocation == 0')
                cash_allocation = 1
                coin_allocation = 0
                cash_balance = price*coin_balance
                coin_balance = 0





        value = price*coin_balance + cash_balance
        


        portfolio_raw.loc[len(analysis)] = [
            time,
            price,
            difference_30m,
            cash_allocation,
            coin_allocation,
            cash_balance,
            coin_balance,
            value
        ]


        print(portfolio_raw)
        portfolio_raw.to_csv(path(symbol) + 'difference_30m/raw.csv', index=False)

    Misc.printDebug('Difference30m().updateRaw(): FINISHED')

def update(symbol):
    Misc.printDebug('Difference30m().update(): STARTED')
    updateRaw(symbol)
    Misc.printDebug('Difference30m().update(): FINISHED')