import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# Defining constants for columns of data
COL_1 = 0
COL_2 = 1
COL_3 = 2
COL_4 = 3
COL_5 = 4
COL_6 = 5

# Defining experiment constants
P_ATM = 100.07
LAMBDA_O = 283.2


# Read raw data from file
def readData(dirName, filetype, skipRows, yCols):
    fileNames = glob(dirName + '/*.' + filetype)
    fileNames.sort(key=len)
    for file in fileNames:
        print (file)
    data = [np.loadtxt(file, skiprows=skipRows)
            for file in fileNames]
    processedData = []
    for array in data:
        dataPoints = processArray(array, yCols)
        processedData.append(dataPoints)
    return processedData


# Convert each row of data into separate x and y lists
def processArray(array, yCols):
    x = []
    y = []
    for i in range(0, yCols):
        y.append([])
    for i in range(0, len(array)):
        x_data_raw = array[i][COL_1]
        x_data_processed = process_x(x_data_raw)
        x.append(float(x_data_processed))
        # Loop through data to add additional columns
        for j in range(0, yCols):
            # Offset loop value to account for x column
            index_offset = j + 1
            y_data_raw = array[i][index_offset]
            y_data_processed = process_y(y_data_raw)
            y[j].append(float(y_data_processed))
    return [x, y]


# process_x processes a single x value before saving it
def process_x(array):
    return array


# process_y processes a single y value before saving it
def process_y(array):
    return array


# Convert temperature readings from Celsius to Kelvin
def celsius_to_kelvin(celsiusReading):
    return celsiusReading + 273.15


# Convert pressure readings from relative PSI to absolute kPa
# NOTE: p_atm must be in [kPa]
def psi_to_kPa(psiReading, p_atm):
    return (psiReading * 6.8948) + p_atm
