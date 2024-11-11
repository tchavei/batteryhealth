import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger
import numpy as np

# Constants

STEP = 2000
FILE_NAME = 'data.csv'

# Loading data using pandas and sorting values

df = pd.read_csv(FILE_NAME)

df.sort_values('km', ascending=True, inplace=True)

# Define the plot using km and health columns, styles and markers

plt.plot(df['km'], df['health'], color='blue', linestyle='solid', marker='D', label="Battery Health")

# Set limits for the y axis

plt.ylim(60, 100) 

# Set limits for the x axis based on max recorded km, rounded to the nearest 1000
 
max_km = round(df['km'].max(), -3)

# Set the step for the x axis based on the constant STEP

plt.xticks(np.arange(0, max_km + STEP, STEP)) 

# Adding horizontal lines for health thresholds

plt.axhline(y=80, color='orange', linestyle='dashed', label='3 Year Threshold')
plt.axhline(y=70, color='red', linestyle='dashed', label='8 Year Threshold')

# Set a background grid for the plot

plt.grid(which='major', axis='y', zorder=-1.0, color='#eeeeee')
plt.grid(which='major', axis='x', zorder=-1.0, color='#eeeeee')

# Set labels and title for the axes and the plot

plt.xlabel('Km')
plt.ylabel('Battery Health Percentage')
plt.title("Battery Health Over Time")

# Displaying the legend and the plot
plt.legend()
plt.show()