import csv
import os
import numpy as np
import sympy as sy

DEBUG = True

def printDebug(message):
    if DEBUG:
        print(message)
    else:
        pass

def read_csv_to_list(csv_path):
    printDebug('Misc.read_csv_to_list(): STARTED')
    column_names = []
    numerical_array = []
    csv_list = []
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            csv_list.append(line)
    for i in range(len(csv_list)):
        if i == 0:
            column_names = csv_list[0]
        else:
            numerical_array.append(csv_list[i])
    printDebug('Misc.read_csv_to_list(): FINISHED')
    return column_names, numerical_array


def write_list_to_csv(column_names, numerical_array, csv_path):
    printDebug('Misc.write_list_to_csv(): STARTED')
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([column_names])
        writer.writerows(list(numerical_array))
    printDebug('Misc.write_list_to_csv(): FINISHED')


