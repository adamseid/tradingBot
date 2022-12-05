from ...misc import Misc
from .long import Absolute, Split

def update(symbol):
    Misc.printDebug('Long.update(): STARTED')
    Absolute.update(symbol)
    Split.update(symbol)
    Misc.printDebug('Long.update(): FINISHED')


