from ....misc import Misc
from .absolute import Slope


def update(symbol):
    Misc.printDebug('Absolute.update(): STARTED')
    Slope.update(symbol)
    Misc.printDebug('Absolute.update(): FINISHED')

