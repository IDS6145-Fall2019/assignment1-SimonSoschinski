import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

padata = pd.read_csv("Port_Authority_Trans-Hudson_Corporation__PATH__Average_Weekday_and_Weekend_Ridership__Beginning_1996.csv",
                     sep=',', names=["Year", "Month", "Weekday", "Saturday", "Sunday"], header=0)


print(padata.head(5))
print(padata)