import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
  fig, axes = plt.subplots(figsize=(16,6))
  sns.scatterplot(data=df, ax=axes,x="Year", y = "CSIRO Adjusted Sea Level" , palette ="bright").set(title="Rise in Sea Level",xlabel="Year", ylabel="Sea Level (inches)")

    # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df["CSIRO Adjusted Sea Level"])
  df_year = pd.Series(range(1880,2051,1))
  axes.plot(df_year, slope * df_year + intercept, '-')

    # Create second line of best fit
  
  df_2 = df[ df["Year"]>=2000 ]
  slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2["Year"], df_2["CSIRO Adjusted Sea Level"])
  df_year2 = pd.Series(range(2000,2051,1))
  axes.plot(df_year2, slope2 * df_year2 + intercept2, '-')

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()