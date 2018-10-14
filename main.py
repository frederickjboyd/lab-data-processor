import ingest
import plot
import stats

# dirName = input('Directory of data to be plotted: ')
dirName = '../1/Data'
data = ingest.readData(dirName)
plot.plotTemperatureData(data)
plot.plotPressureData(data)
# Calculate total mass using flow rate data for part 2
m_run_1 = stats.calculateTotalMass(data[2])
m_run_2 = stats.calculateTotalMass(data[3])
print 'total m (run 1):', m_run_1
print 'total m (run 2):', m_run_2
