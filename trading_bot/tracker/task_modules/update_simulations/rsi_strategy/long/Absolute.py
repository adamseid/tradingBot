from ....misc import Misc
from .absolute import Trigger3366, Trigger3366Delayed
from .absolute import Trigger5050

def update(symbol):
    Misc.printDebug('Absolute.update(): STARTED')
    Trigger3366.update(symbol)
    Trigger5050.update(symbol)
    Trigger3366Delayed.update(symbol)
    Misc.printDebug('Absolute.update(): FINISHED')

