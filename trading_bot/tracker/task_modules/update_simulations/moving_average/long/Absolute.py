
from ....misc import Misc
from .absolute import OverUnder


def update(symbol):
    Misc.printDebug('Absolute.update(): STARTED')
    OverUnder.update(symbol)
    Misc.printDebug('Absolute.update(): FINISHED')

