import numpy as np 
import sys
import os.path
import peak_estimation.peak_est_main
import peak_estimation.peak_est_calc

#Locate dataset
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'peak_estimation/voltage_data.csv')

# Instantiate PeakEstMain as sensor_data
sensor_data = peak_estimation.peak_est_main.PeakEstMain(filename)
data = sensor_data.data_as_csv  # Return the sensore data as a dataframe
voltage = data.iloc[:, 1]  # Return the voltage column for manipulation with the peak estimation algorithm

# Instantiate Real_time_peak_detection as peaks
peaks = peak_estimation.peak_est_calc.Real_time_peak_detection(voltage, 50, 3.5, 0.5)
print(peaks.thresholding_algo(5))  #Return a positive or negative classification for a true peak




