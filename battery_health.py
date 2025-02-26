import os
import json
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
import numpy as np

# Load environment variables
load_dotenv()

# Constants
CHART_LIMITS = json.loads(os.getenv('CHART_LIMITS'))
STEP = int(os.getenv('STEP'))
FILE_NAME = os.getenv('FILE_NAME')
THRESHOLD_LEVELS = json.loads(os.getenv('THRESHOLD_LEVELS'))
THRESHOLD_LABELS = json.loads(os.getenv('THRESHOLD_LABELS'))

def load_and_prepare_data(file_name):
    """
    Load data from CSV and sort by 'km'.
    
    :param file_name: Name of the file to load the data from.
    :return: Pandas DataFrame sorted by 'km'.
    """
    df = pd.read_csv(file_name)
    df.sort_values('km', ascending=True, inplace=True)
    return df

def plot_battery_health_over_time(df, chart_limits, step, threshold_levels, threshold_labels):
    """
    Plots battery health over time with thresholds.
    
    :param df: DataFrame containing the data.
    :param chart_limits: List with 2 elements for y-axis limits.
    :param step: Step for x-axis ticks.
    :param threshold_levels: Levels for health thresholds.
    :param threshold_labels: Labels for the health thresholds.
    """

    # Plotting 'km' vs. 'health'
    plt.plot(df['km'], df['health'], color='blue', linestyle='solid', marker='D', label="Battery Health")

    # Setting chart limits for both axes
    plt.ylim(chart_limits[0], chart_limits[1])

    # Rounding max 'km' to the nearest step and setting x-axis limits
    max_km = round(df['km'].max(), + step)
    plt.xticks(np.arange(0, max_km + step, step))
    
    # Adding threshold lines
    for level, label in zip(threshold_levels, threshold_labels):
        plt.axhline(y=level, color='red' if label.lower().startswith('8') else 'orange', linestyle='dashed', label=label)
    
    # Enhancing chart readability
    plt.grid(which='major', axis='y', linestyle='-', color='#eeeeee', zorder=-1.0)
    plt.grid(which='major', axis='x', linestyle='-', color='#eeeeee', zorder=-1.0)
    
    # Labeling axes and setting title
    plt.xlabel('Kilometers (km)')
    plt.ylabel('Battery Health (%)')
    plt.title("Battery Health Over Kilometers")
    
    # Displaying the legend and plot
    plt.legend()
    plt.show()

def main():
    """
    Main function to execute script tasks.
    """
    # Load and prepare data
    df = load_and_prepare_data(FILE_NAME)
    
    # Plotting the data
    plot_battery_health_over_time(df, CHART_LIMITS, STEP, THRESHOLD_LEVELS, THRESHOLD_LABELS)

if __name__ == "__main__":
    main()
