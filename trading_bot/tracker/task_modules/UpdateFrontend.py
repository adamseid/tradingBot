from .misc import Misc
import pandas as pd
from .update_frontend import Current, Graph

def update():
    Misc.printDebug('UpdateFrontend.update(): STARTED')
    state = pd.read_csv('./tracker/task_modules/state.csv')
    print(state)
    if state['filename'][0] == 'none':
        print('filename == none')
    else:
        print('filename != none')
        Current.update(state['path'][0])
        Graph.update(state['path'][0])
    Misc.printDebug('UpdateFrontend.update(): FINISHED')