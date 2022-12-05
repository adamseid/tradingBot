from ..misc import Misc
from .rsi_strategy.onetime import Onetime
from .rsi_strategy import Longshort
from .rsi_strategy import Long
import os
import pandas as pd
import time

def update(symbols):
    Misc.printDebug('RSIStrategy.update(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ', symbol)
        #Onetime.update(symbol)
        #Longshort.update(symbol)
        Long.update(symbol)
       

    Misc.printDebug('RSIStrategy.update(): FINISHED')