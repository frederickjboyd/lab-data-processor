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


# Read raw data from file
def readData(dirName, filetype, skipRows):
    fileNames = glob(dirName + '/*.' + filetype)
    fileNames.sort(key=len)
    for file in fileNames:
        print (file)
    data = [np.loadtxt(file, skiprows=skipRows) for file in fileNames]
    processedData = []
    for array in data:
        dataPoints = processArray(array)
        processedData.append(dataPoints)
    return processedData


def processArray(array):
    t = []
    y_1 = []
    for i in range(0, len(array)):
        col_1_data = array[i][COL_1]
        col_2_data = array[i][COL_2]
        # Converting temperature data from Celsius to Kelvin
        t.append(float(col_1_data))
        y_1.append(float(col_2_data))
    return [t, [y_1]]


# Convert temperature readings from Celsius to Kelvin
def celsius_to_kelvin(celsiusReading):
    return celsiusReading + 273.15


# Convert pressure readings from relative PSI to absolute kPa
# NOTE: p_atm must be in [kPa]
def psi_to_kPa(psiReading, p_atm):
    return (psiReading * 6.8948) + p_atm
