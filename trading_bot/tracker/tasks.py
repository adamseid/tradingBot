from celery import shared_task
#from tradingview_ta import TA_Handler, Interval
from .task_modules import UpdateTables
from .task_modules import UpdateSimulations, UpdateRaw, UpdateAnalysis
from .task_modules import BackupTables, BackupSimulations
from .task_modules import UpdateFrontend
#from .task_modules.update_analysis.price_average.price_average_5m.dprice_1m.dprice_average_1m.ddprice_1m import ddPriceAverage5m as Test


from .task_modules.misc import Misc

@shared_task()
def update():
    print('\n', 'tasks.update(): STARTED')
    symbols = ['BTCUSDT', 'ETHUSDT','BTCUPUSDT', 'BTCDOWNUSDT']

    UpdateRaw.update(symbols)
    UpdateAnalysis.update(symbols)
    UpdateSimulations.update(symbols)

    #UpdateFrontend.update()



    print('tasks.update(): FINISHED')

@shared_task()
def backup():
    Misc.printDebug('tasks.backup(): STARTED')
    symbols = ['BTCUSDT', 'ETHUSDT','BTCUPUSDT', 'BTCDOWNUSDT']
    BackupTables.backupTables(symbols)
    #BackupSimulations.backup(symbols)


    Misc.printDebug('tasks.backup(): FINISHED')




@shared_task()
def test():
    Misc.printDebug('tasks.test(): STARTED')
    symbols = ['BTCUSDT', 'ETHUSDT','BTCUPUSDT', 'BTCDOWNUSDT']
    
    for symbol in symbols: 
        pass
    
    UpdateFrontend.update()
    #Test.update(['BTCUSDT', 'ETHUSDT'])

    Misc.printDebug('tasks.test(): FINISHED')

