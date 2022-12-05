from ..misc import Misc
import pandas as pd
import os
import time

from asgiref.sync import sync_to_async, async_to_sync
from channels.layers import get_channel_layer


def update(path):
    Misc.printDebug('Current.update(): STARTED')
    #print(path)
    perp = pd.read_csv(path)
    #print(perp)
    column_names = list(perp.columns.values)
    #print(column_names)
    last_row = perp.values[-1].tolist()
    #print(last_row)

    message = {
        'type': 'updateCurrent',
        'data': {
            'location': [''],
            'time': time.time(),
            'column_names': column_names,
            'last_row': last_row
        }
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('crypto', message)

    Misc.printDebug('Current.update(): FINISHED')


