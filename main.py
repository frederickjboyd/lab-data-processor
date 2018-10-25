import ingest
import plot
import stats

# dirName = input('Directory of data to be plotted: ')
dirName = ''
data = ingest.readData(dirName, 'csv', 1)
