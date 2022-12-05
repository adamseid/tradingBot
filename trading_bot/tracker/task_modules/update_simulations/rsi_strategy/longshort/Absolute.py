from ....misc import Misc
from .absolute import Split5050


def update(symbol):
    Misc.printDebug('Absolute.update(): STARTED')
    Split5050.update(symbol)
    Misc.printDebug('Absolute.update(): FINISHED')