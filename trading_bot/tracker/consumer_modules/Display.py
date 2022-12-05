from ..task_modules.misc import Misc
import pandas as pd


def connect(data):
    Misc.printDebug('Display.connect(): STARTED')
    print(data)

    state = pd.read_csv('./tracker/task_modules/state.csv')
    print(state)
    state['filename'][0] = data['filename']
    state['path'][0] = data['path']

    state.to_csv('./tracker/task_modules/state.csv', index=False)
    Misc.printDebug('Display.connect(): FINISHED')
    return data

