import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from loguru import logger
import numpy as np
from dotenv import load_dotenv

# Constants

load_dotenv()

CHART_LIMITS = json.loads(os.getenv('CHART_LIMITS'))
STEP = int(os.getenv('STEP'))
FILE_NAME = os.getenv('FILE_NAME')
THRESHOLD_LEVELS = json.loads(os.getenv('THRESHOLD_LEVELS'))
THRESHOLD_LABELS = json.loads(os.getenv('THRESHOLD_LABELS'))


# Loading data using pandas and sorting values

df = pd.read_csv(FILE_NAME)

df.sort_values('km', ascending=True, inplace=True)

# Define the plot using km and health columns, styles and markers

plt.plot(df['km'], df['health'], color='blue', linestyle='solid', marker='D', label="Battery Health")

# Set limits for the y axis

plt.ylim(CHART_LIMITS[0], CHART_LIMITS[1])

# Set limits for the x axis based on max recorded km, rounded to the nearest 1000
 
max_km = round(df['km'].max(), -3)

# Set the step for the x axis based on the constant STEP

plt.xticks(np.arange(0, max_km + STEP, STEP)) 

# Adding horizontal lines for health thresholds

plt.axhline(y=THRESHOLD_LEVELS[0], color='orange', linestyle='dashed', label=THRESHOLD_LABELS[0])
plt.axhline(y=THRESHOLD_LEVELS[1], color='red', linestyle='dashed', label=THRESHOLD_LABELS[1])

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