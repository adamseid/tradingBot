from ..misc import Misc
from .opposite import Long
import os
import pandas as pd
import time

def update(symbols):
    Misc.printDebug('Opposite.update(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ', symbol)
        Long.update(symbol)
       

    Misc.printDebug('Opposite.update(): FINISHED')