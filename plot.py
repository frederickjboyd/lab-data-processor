import matplotlib.pyplot as plt
import numpy as np


def convertTimeToIndex(time, dt):
    return time * (1 / dt)


# Generates basic plot for two variables
# X           {list} Contains X values of data
# Y           {list} Contains list of Y values of data
# fit         {list} Contains coefficients of the polynomial best fit (ordered
#             from highest degree coefficient to lowest degree coefficient)
# title       {string} Title of plot
# x_label     {string} x-axis label
# y_label     {string} y-axis label
# data_legend {string} Label to use in legend for data being plotted
# plotFit     {boolean} Determines whether a best fit should be plotted
# saveDir     {string} Directory to save plots
def plotData(dataSet, y_err, bestFit, title, x_label, y_label, data_legend, plotFit, saveDir):
    for i in range(0, len(dataSet)):
        X = dataSet[i][0]
        Y = dataSet[i][1]
        if plotFit:
            for j in range(0, len(Y)):
                plt.scatter(X, Y[j], color='black', s=1, label=data_legend)
                # plt.errorbar(X, Y[i], yerr=y_err, color='black', fmt='o',
                #  markersize=2, linewidth=1, label=data_legend)
                x_fit, y_fit = calculatePrettyBestFit(X, bestFit[i], 100)
                plt.plot(x_fit, y_fit, '--', label="Best Fit")
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.legend()
        plt.savefig(saveDir + '/' + 'plot-' + str(i), dpi=300)
        plt.close()


def plotResiduals(dataSet, col, bestFit, title, x_label, y_label, saveDir):
    for i in range(0, len(dataSet)):
        X = dataSet[i][0]
        Y = dataSet[i][1][col]
        a = bestFit[i][0]
        b = bestFit[i][1]
        expected = [a * x_i + b for x_i in X]
        residuals = []
        for j in range(0, len(Y)):
            residual = Y[j] - expected[j]
            residuals.append(residual)
        plt.scatter(X, residuals, color='black', s=1)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.savefig(saveDir + '/' + 'residual-' + str(i), dpi=300)
        plt.close()


def calculatePrettyBestFit(X, fit, points):
    a = fit[0]
    b = fit[1]
    c = fit[2]  # ONLY FOR POLYNOMIAL FIT IN AER LAB - REMOVE THIS LATER
    x_min = min(X)
    x_max = max(X)
    x_spaced = np.linspace(x_min, x_max, points)
    y_fit = [a * (x_i ** 2) + b * x_i + c for x_i in x_spaced]
    return [x_spaced, y_fit]
