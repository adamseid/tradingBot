from ....misc import Misc
from .absolute import Slope

def backup(symbol):
    Misc.printDebug('Absolute.backup(): STARTED')
    Slope.backup(symbol)
    Misc.printDebug('Absolute.backup(): FINISHED')

