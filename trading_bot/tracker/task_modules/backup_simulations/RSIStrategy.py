from ..misc import Misc
from .rsi_strategy import Long


def backup(symbols):
    Misc.printDebug('RSIStrategy.backup(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ' +  symbol)
        Long.backup(symbol)
    Misc.printDebug('RSIStrategy.backup(): FINISHED')





