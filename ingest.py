import numpy as np
import matplotlib.pyplot as plt
from os.path import basename
from glob import glob

# Defining constants for columns of data
COL_1 = 0

# Defining experimental constants
P_ATM = 100.07
LAMBDA_O = 283.2


# Read raw data from file
def readData(dirName, filetype, skipRows):
    # Finding all files in specified directory with the extension "filetype"
    files = glob(dirName + '/*.' + filetype)
    files.sort(key=len)
    # Initializing variables
    fileDirectories = []
    processedData = []
    for file in files:
        fileDirectories.append(str(file))
        # Showing user which files are being processed
        print str(file)
    fileNames = extractFileName(fileDirectories, filetype)
    # Loading data
    data = [np.loadtxt(file, skiprows=skipRows) for file in files]
    # Checking that data loaded properly
    if len(data) == 0:
        return False
    for array in data:
        dataPoints = processArray(array)
        processedData.append(dataPoints)
    return processedData, fileNames


# Convert each row of data into separate x and y lists
def processArray(array):
    x = []
    y = []
    # Determining number of y columns in data (subtract 1 to account for x column)
    yCols = len(array[0]) - 1
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


def extractFileName(fileDirectories, filetype):
    fileNames = []
    # Add 1 to account for '.' before extension
    extensionLength = len(filetype) + 1
    for directory in fileDirectories:
        fileName = basename(directory)
        fileNames.append(fileName[:len(fileName) - extensionLength])
    return fileNames
