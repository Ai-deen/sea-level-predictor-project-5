import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(16,6))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err =linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    line_x = np.arange(df['Year'].min(), 2050,1)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y)
    

    # Create second line of best fit
    df1 = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err =linregress(df1['Year'], df1['CSIRO Adjusted Sea Level'])
    line_x = np.arange(2000, 2050)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
