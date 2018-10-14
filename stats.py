from scipy.stats import chisquare
import numpy as np


# Defining constants for columns of data
TIME_COL = 0
T1_COL = 1
T2_COL = 2
P1_COL = 3
P2_COL = 4
M_FLOWRATE_COL = 5


def reducedChiSquared(data, bestFit, uncertainty):
    # Check if there is a best fit for each set of data
    if len(bestFit) != len(data):
        return False
    chi_squared_reduced = []
    # expectedValues = calculateExpectedValues(data, bestFit)
    # Calculate degree of polynomial best fit
    # degree = len(bestFit) - 1
    for i in range(0, len(data)):
        X = data[i][0]
        Y = data[i][1]
        a = bestFit[i][0]
        b = bestFit[i][1]
        accum = 0
        # Check if there's any length discrepancies between the inputs
        if len(X) != len(Y):
            return False
        expected = [a * x_i + b for x_i in X]
        freedom = degreesOfFreedom(X)
        for i in range(0, len(Y)):
            accum += ((expected[i] - Y[i]) ** 2) / (uncertainty ** 2)
        chi_squared_reduced.append(accum / freedom)
    return chi_squared_reduced


def degreesOfFreedom(data):
    return len(data) - 2


def calculateTotalMass(data):
    accum = 0
    dt = 0.1
    for i in range(0, len(data[M_FLOWRATE_COL])):
        accum += data[M_FLOWRATE_COL][i] * dt
    return accum


def fitData(data, degree):
    bestFits = []
    for i in range(0, len(data)):
        x = data[i][0]
        y = data[i][1]
        poly = np.polyfit(x, y, degree)
        bestFits.append(poly)
    return bestFits
