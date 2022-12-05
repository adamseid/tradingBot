from ..misc import Misc
from .momentum import Long



def backup(symbols):
    Misc.printDebug('Momentum.backup(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ' +  symbol)
        Long.backup(symbol)
    Misc.printDebug('Momentum.backup(): FINISHED')



