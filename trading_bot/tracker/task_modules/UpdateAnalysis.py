from .misc import Misc
from .update_analysis import PriceAverage

def update(symbols):
    Misc.printDebug('UpdateAnalysis.update(): STARTED')
    PriceAverage.update(symbols)
    Misc.printDebug('UpdateAnalysis.update(): FINISHED')