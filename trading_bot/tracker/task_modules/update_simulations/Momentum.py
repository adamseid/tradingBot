from ..misc import Misc
from .momentum import Long
import os
import pandas as pd
import time

def update(symbols):
    Misc.printDebug('Momentum.update(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ', symbol)
        #Onetime.update(symbol)
        #Longshort.update(symbol)
        Long.update(symbol)
       

    Misc.printDebug('Momentum.update(): FINISHED')