import matplotlib.pyplot as plt


# Defining constants for columns of data
TIME_COL = 0
T1_COL = 1
T2_COL = 2
P1_COL = 3
P2_COL = 4
M_FLOWRATE_COL = 5


def convertTimeToIndex(time):
    return time * 10


# Defining constants for ranges of time to display on plots
START_0 = convertTimeToIndex(380)
END_0 = convertTimeToIndex(390)
# END_0 = convertTimeToIndex(350)
START_1 = convertTimeToIndex(230)
START_2 = convertTimeToIndex(0)
END_2 = convertTimeToIndex(500)
START_3 = convertTimeToIndex(0)
END_3 = convertTimeToIndex(500)


def plotTemperatureData(dataSet):
    for i in range(0, len(dataSet)):
        t = dataSet[i][TIME_COL]
        T1 = dataSet[i][T1_COL]
        T2 = dataSet[i][T2_COL]
        # Adjusting time scale
        if (i != 0):
            t, T1, T2 = customTimeScale(t, T1, T2, i, False)
        else:
            t, T1, T2 = customTimeScale(t, T1, T2, i, True)
        plt.scatter(t, T1, color='black', s=1, label='T1')
        # Only plot data for first container in part 2
        if (i != 2 and i != 3):
            plt.scatter(t, T2, color='blue', s=1, label='T2')
        plt.xlabel('Time [s]')
        plt.ylabel('Temperature [K]')
        title = handlePlotTitle(i)
        plt.title(title)
        plt.legend()
        plt.savefig('../1/Plots/' + 'run-temperature-' + str(i), dpi=300)
        plt.close()


def plotPressureData(dataSet):
    for i in range(0, len(dataSet)):
        t = dataSet[i][TIME_COL]
        P1 = dataSet[i][P1_COL]
        P2 = dataSet[i][P2_COL]
        # Adjusting time scale
        t, P1, P2 = customTimeScale(t, P1, P2, i, False)
        plt.scatter(t, P1, color='green', s=1, label='P1')
        # Only plot data for first container in part 2
        if (i != 2 and i != 3):
            plt.scatter(t, P2, color='red', s=1, label='P2')
        plt.xlabel('Time [s]')
        plt.ylabel('Absolute Pressure [kPa]')
        title = handlePlotTitle(i)
        plt.title(title)
        plt.legend()
        plt.savefig('../1/Plots/' + 'run-pressure-' + str(i), dpi=300)
        plt.close()


def plotDataWithFit(dataSet, bestFit):
    for i in range(0, len(dataSet)):
        X = dataSet[i][0]
        Y = dataSet[i][1]
        a = bestFit[i][0]
        b = bestFit[i][1]
        yFit = [a * x_i + b for x_i in X]
        plt.scatter(X, Y, color='black', s=1, label="Data")
        plt.plot(X, yFit, '--', label="Best Fit")
        plt.xlabel('CHANGEME [units]')
        plt.ylabel('CHANGEME [units]')
        plt.title('Run ' + str(i))
        plt.legend()
        plt.savefig('../1/Plots/' + 'run-' + str(i), dpi=300)
        plt.close()


def plotResiduals(dataSet, bestFit):
    for i in range(0, len(dataSet)):
        X = dataSet[i][0]
        Y = dataSet[i][1]
        a = bestFit[i][0]
        b = bestFit[i][1]
        expected = [a * x_i + b for x_i in X]
        residuals = []
        for j in range(0, len(Y)):
            residual = Y[j] - expected[j]
            residuals.append(residual)
        plt.scatter(X, residuals, color='black', s=1)
        plt.xlabel('CHANGEME [units]')
        plt.ylabel('CHANGEME [units]')
        plt.title('Run ' + str(i) + ' Residual Plot')
        plt.savefig('DIRECTORY' + 'run-' + str(i), dpi=300)
        plt.close()


def handlePlotTitle(index):
    if index == 0:
        return "Equalizing Two Tanks using a Center Solenoid Valve"
    elif index == 1:
        return "Equalizing Two Tanks using a Micrometer Value"
    elif index == 2:
        return "Part 2 - Run 1 (old)"
    elif index == 3:
        return "Pressurization of Left Tank"
    else:
        return ""


def customTimeScale(timeData, data1, data2, index, goToEnd):
    if index == 0 and goToEnd == True:
        timeData = timeData[START_0:]
        data1 = data1[START_0:]
        data2 = data2[START_0:]
    elif index == 0:
        timeData = timeData[START_0:END_0]
        data1 = data1[START_0:END_0]
        data2 = data2[START_0:END_0]
    elif index == 1:
        timeData = timeData[START_1:]
        data1 = data1[START_1:]
        data2 = data2[START_1:]
    elif index == 2:
        timeData = timeData[START_2:END_2]
        data1 = data1[START_2:END_2]
        data2 = data2[START_2:END_2]
    elif index == 3:
        timeData = timeData[START_3:END_3]
        data1 = data1[START_3:END_3]
        data2 = data2[START_3:END_3]
    return [timeData, data1, data2]
