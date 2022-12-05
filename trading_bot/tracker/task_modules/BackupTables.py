from .misc import Misc
import time


def backupTables(symbols):
    Misc.printDebug('BackupTables.backupTables(): STARTED')
    
   

    for symbol in symbols:
        csv_path = '../storage/crypto/BINANCE/tables/current/raw/' + symbol + '.csv'
        column_names, numerical_array = Misc.read_csv_to_list(csv_path)
        backup_path = '../storage/crypto/BINANCE/tables/backup/' + symbol + '/' + str(int(round(time.time(), 0))) + '.csv'
        Misc.write_list_to_csv(column_names, numerical_array, backup_path)

    

    Misc.printDebug('BackupTables.backupTables(): FINISHED')
