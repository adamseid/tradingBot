from ..misc import Misc
import pandas as pd
import os
import time

from asgiref.sync import sync_to_async, async_to_sync
from channels.layers import get_channel_layer

def getLastFewRows(simulation, column_names):
    Misc.printDebug('Graph.getLastFewRows(): STARTED')

    last_few_rows = []

    num_of_rows = 24*60

    simulation = simulation.tail(num_of_rows)


    for column_name in column_names:
        #print(simulation[column_name].tolist())
        last_few_rows.append(simulation[column_name].tolist())

    #print(last_few_rows)

    Misc.printDebug('Graph.getLastFewRows(): FINISHED')
    return last_few_rows


def update(path):
    Misc.printDebug('Graph.update(): STARTED')
    simulation = pd.read_csv(path)
    column_names = list(simulation.columns.values)
    #last_row = perp.values[-1].tolist()
    last_few_rows = getLastFewRows(simulation, column_names)

    message = {
        'type': 'updateGraph',
        'data': {
            'location': [''],
            'time': time.time(),
            'column_names': column_names,
            'last_few_rows': last_few_rows
        }
    }
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('crypto', message)

    Misc.printDebug('Graph.update(): FINISHED')


