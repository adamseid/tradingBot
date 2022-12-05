from ..misc import Misc
from .price_average import PriceAverage1m, PriceAverage5m, PriceAverage30m, PriceAverage4h, PriceAverage5m

def update(symbols):
    Misc.printDebug('PriceAverage.update(): STARTED')
    PriceAverage1m.update(symbols)
    PriceAverage5m.update(symbols)
    PriceAverage30m.update(symbols)
    PriceAverage4h.update(symbols)
    Misc.printDebug('PriceAverage.update(): FINISHED')