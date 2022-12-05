from ...misc import Misc
from .longshort import Absolute
import pandas as pd
import time


def update(symbol):
    Misc.printDebug('Longshort.update(): STARTED')
    Absolute.update(symbol)

    
    
    Misc.printDebug('Longshort.update(): FINISHED')
    

