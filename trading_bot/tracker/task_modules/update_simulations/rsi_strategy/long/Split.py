
from ....misc import Misc
from .split import OnParRSI


def update(symbol):
    Misc.printDebug('Split.update(): STARTED')
    OnParRSI.update(symbol)
    Misc.printDebug('Split.update(): FINISHED')

