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


# Read raw data from file
def readData(dirName, filetype):
    fileNames = glob(dirName + '/*.txt')
    fileNames.sort(key=len)
    for file in fileNames:
        print (file)
    data = [np.loadtxt(file, skiprows=4) for file in fileNames]
    processedData = []
    for array in data:
        dataPoints = processArray(array)
        processedData.append(dataPoints)
    return processedData


def processArray(array):
    t = []
    y_1 = []
    y_2 = []
    y_3 = []
    y_4 = []
    y_5 = []
    for i in range(0, len(array)):
        col_1_data = array[i][COL_1]
        col_2_data = array[i][COL_2]
        col_3_data = array[i][COL_3]
        col_4_data = array[i][COL_4]
        col_5_data = array[i][COL_5]
        col_6_data = array[i][COL_6]
        # Converting temperature data from Celsius to Kelvin
        col_1_data = celsius_to_kelvin(col_1_data)
        col_2_data = celsius_to_kelvin(col_2_data)
        col_3_data = psi_to_kPa(col_3_data)
        col_4_data = psi_to_kPa(col_4_data)
        t.append(float(col_1_data))
        y_1.append(float(col_2_data))
        y_2.append(float(col_3_data))
        y_3.append(float(col_4_data))
        y_4.append(float(col_5_data))
        y_5.append(float(col_6_data))
    return [t, y_1, y_2, y_3, y_4, y_5]


# Convert temperature readings from Celsius to Kelvin
def celsius_to_kelvin(celsiusReading):
    return celsiusReading + 273.15


# Convert pressure readings from relative PSI to absolute kPa
# NOTE: p_atm must be in [kPa]
def psi_to_kPa(psiReading, p_atm):
    return (psiReading * 6.8948) + p_atm
