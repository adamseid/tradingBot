from .misc import Misc
from .update_simulations import RSIStrategy, MACDStrategy, Momentum, MovingAverage, Opposite



def update(symbols):
    Misc.printDebug('UpdateSimulations.update(): STARTED')
    RSIStrategy.update(symbols)
    MACDStrategy.update(symbols)
    Momentum.update(symbols)
    MovingAverage.update(symbols)
    Opposite.update(symbols)
    Misc.printDebug('UpdateSimulations.update(): FINISHED')

