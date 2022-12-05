from ....misc import Misc
from .absolute import Trigger3366, Trigger5050, Trigger3366Delayed

def backup(symbol):
    Misc.printDebug('Absolute.backup(): STARTED')
    Trigger5050.backup(symbol)
    Trigger3366.backup(symbol)
    Trigger3366Delayed.backup(symbol)
    Misc.printDebug('Absolute.backup(): FINISHED')

