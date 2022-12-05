from ..misc import Misc
from .macd_strategy import Long



def backup(symbols):
    Misc.printDebug('MACDStrategy.backup(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ' +  symbol)
        Long.backup(symbol)
    Misc.printDebug('MACDStrategy.backup(): FINISHED')



