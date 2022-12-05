from .misc import Misc
from .backup_simulations import RSIStrategy
from .backup_simulations import MACDStrategy, Momentum



def backup(symbols):
    Misc.printDebug('BackupSimulations.backup(): STARTED')
    
    RSIStrategy.backup(symbols)
    MACDStrategy.backup(symbols)
    Momentum.backup(symbols)


    Misc.printDebug('BackupSimulations.backup(): FINISHED')
