from ..task_modules.misc import Misc
import pandas as pd
import os

def run():
    Misc.printDebug('Connect.run(): STARTED')

    #print(os.listdir('./tracker/task_modules'))

    state = pd.read_csv('./tracker/task_modules/state.csv')
    print(state)

    state['filename'][0] = 'none'
    state['path'][0] = 'none'

    state.to_csv('./tracker/task_modules/state.csv', index=False)



    Misc.printDebug('Connect.run(): FINISHED')


