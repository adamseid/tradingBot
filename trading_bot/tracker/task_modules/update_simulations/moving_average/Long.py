from ...misc import Misc
from .long import Absolute

def update(symbol):
    Misc.printDebug('Long.update(): STARTED')
    Absolute.update(symbol)
    Misc.printDebug('Long.update(): FINISHED')


