from ....misc import Misc
import pandas as pd
import time


def update(symbol):
    Misc.printDebug('Onetime.update(): STARTED')
    
    data = pd.read_csv('../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv')
    time_new = time.time()
    price_new = data['close'][len(data['close'])-1]
    rsi_new = data['rsi'][len(data['rsi'])-1]
    change_cash_new = -1/5 * rsi_new + 10
    change_coin_new = change_cash_new/price_new
    filename = '1000USD_2022-10-23'
    simulation_current = pd.read_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/onetime/' + symbol + '/' + filename + '.csv')

    # Initial Run
    if str(simulation_current['balance_coin'][len(simulation_current)-1]) == 'x':
        balance_BTC = float(simulation_current['balance_USDT'][len(simulation_current)-1]) / float(price_new)
        simulation_current['balance_coin'][len(simulation_current)-1] = balance_BTC
        simulation_current['price'][len(simulation_current)-1] = price_new
        simulation_current.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/onetime/' + symbol + '/' + filename + '.csv', index=False)

    else:
        balance_USDT_new = price_new * float(simulation_current['balance_coin'][len(simulation_current['balance_coin'])-1]) + change_cash_new
        balance_coin_new = float(simulation_current['balance_coin'][len(simulation_current['balance_coin'])-1]) + change_coin_new
        profit = float(simulation_current['balance_USDT'][len(simulation_current['balance_USDT'])-1]) - float(simulation_current['change_cash'][len(simulation_current['change_cash'])-1]) - float(simulation_current['balance_USDT'][len(simulation_current['balance_USDT'])-2])
        total_profit = simulation_current['profit'].sum()

        simulation_current.loc[len(simulation_current)] = [
            time_new,
            price_new,
            rsi_new,
            change_cash_new,
            change_coin_new,
            balance_USDT_new,
            balance_coin_new,
            profit,
            total_profit
        ]


        simulation_current.to_csv('../storage/crypto/BINANCE/tables/current/simulations/rsi/onetime/' + symbol + '/' + filename + '.csv', index=False)

    

    Misc.printDebug('Onetime.update(): FINISHED')