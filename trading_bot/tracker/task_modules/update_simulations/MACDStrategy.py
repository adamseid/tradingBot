from ..misc import Misc

from .macd_strategy import Long
import os
import pandas as pd
import time

def update(symbols):
    Misc.printDebug('MACDStrategy.update(): STARTED')
    for symbol in symbols:
        print('Current Simulation: ', symbol)

        Long.update(symbol)
       

    Misc.printDebug('MACDStrategy.update(): FINISHED')