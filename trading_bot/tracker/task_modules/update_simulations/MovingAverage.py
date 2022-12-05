from ..misc import Misc

from .moving_average import Long
import os
import pandas as pd
import time

def update(symbols):
    Misc.printDebug('MovingAverage.update(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ', symbol)
        Long.update(symbol)
       

    Misc.printDebug('MovingAverage.update(): FINISHED')