import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
# Loading the data
padata = pd.read_csv('Port_Authority_Trans-Hudson_Corporation__PATH__Average_Weekday_and_Weekend_Ridership__Beginning_1996.csv',
                     sep=',', names=["Year", "Month", "Weekday", "Saturday", "Sunday"], header=0)

# Re-ordering the data by year and month
padata_sorted = padata.sort_values(['Year', 'Month'])
# Creating date format for plot x axis
padata_sorted['Date'] = padata['Year'].map(str) + '-' + padata['Month'].map(str)
padata_sorted['Date'] = pd.to_datetime(padata_sorted['Date'], format = '%Y-%m')
#

# Calculating some statistics
# Means
wdmean = np.mean(padata["Weekday"])
satmean = np.mean(padata["Saturday"])
sunmean = np.mean(padata["Sunday"])
totalmean = np.mean([wdmean, satmean, sunmean])

# STDs
wdstd = np.std(padata["Weekday"])
satstd = np.std(padata["Saturday"])
sunstd = np.std(padata["Sunday"])
totalstd = np.std([wdstd, satstd, sunstd])



# Looking at the data head
print(padata_sorted.head(5))



# Printing some stats
print("The mean ridership on a weekday is " + str(wdmean) + ", for a Saturday " + str(satmean) + " and for a Sunday "
      + str(sunmean) + ". The total mean is " + str(totalmean) + ".")

print("The standard deviation for a weekday is " + str(wdstd) + ", for a Saturday " + str(satstd) + " and for a Sunday "
      + str(sunstd) + ". The total std is " + str(totalstd) + ".")

# Plotting

ywd = padata_sorted["Weekday"]
ysat = padata_sorted["Saturday"]
ysun = padata_sorted["Sunday"]
x = padata_sorted["Date"]

plt.plot(x, ywd, label="Weekdays")
plt.plot(x, ysat, label="Saturdays")
plt.plot(x, ysun, label="Sundays")

plt.title("Trans Hudson Ridership Data")
plt.ylabel("Average Ridership")
plt.xlabel("Year")

plt.legend()

plt.show()

