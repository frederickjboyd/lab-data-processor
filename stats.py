import numpy as np


def reducedChiSquared(dataSet, bestFit, uncertainty):
    # Check if there is a best fit for each set of data
    if len(bestFit) != len(dataSet):
        return False
    chi_squared_reduced = []
    # expectedValues = calculateExpectedValues(data, bestFit)
    # Calculate degree of polynomial best fit
    # degree = len(bestFit) - 1
    for i in range(0, len(dataSet)):
        X = dataSet[i][0]
        Y = dataSet[i][1]
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


def integrate(X, Y, dt):
    if len(X) != len(Y):
        return False
    accum = 0
    for i in range(0, len(Y)):
        accum += Y[i] * dt
    return accum


def fitData(dataSet, degree):
    bestFits = []
    for i in range(0, len(dataSet)):
        x = dataSet[i][0]
        y = dataSet[i][1]
        for j in range(0, len(y)):
            poly = np.polyfit(x, y[j], degree)
            bestFits.append(poly)
        return bestFits
