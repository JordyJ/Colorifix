
Jordan Juritz - Colorifix technical test. 
## Setup

This repo uses poetry for package management. 
The main results are in main.ipynb. Importing functions are in tools.py.

## Methods

In this exercise, I estimate the concentration of an unknown pigment from an absorption spectrum by linear interpolation from a calibration dataset. 

## Part 1
First, I focus on the calibration dataset and I perform some simple visualisations. 
I calculate the absorbtion of the calibration pigment by subtracting the averaged background absorption at each wavelength, assuming that the absorbtion of multiple chemicals in solution combine linearly. 

Then, by inspection of plots, I observe that below a threshold value, the absorbtion data is messy, likely due to the sensitivity of the machine, and there is a central peak in absorbtion that increases with concentration. 
I limit the data to around this peak. 

Using the Beer-Lambert equation, I show that around the peak the absorbance measurements for different concentrations all collapse onto a single function, the absorptivity coefficient. This supports the conclusion that the Absorptivity coefficient is not a function of concentration, and, within the concentrations measured, the absorbtion is a approximately a linear function of concentration. 

## Part 2
I perform some simple visualisations of the sample dataset in which the concentration of pigment is unknown. Checking that the calibration and sample datasets have near-identical background signals shows that the gain of the measurement system has not been changed, and hence the absorbtion measurements are on the same scale. 

As in the calibration dataset, I remove the background signal again and limit the dataset to the peak. 

Having previously confirmed that the Absorptivity coefficient is not a function of concentration, I use it to linearly interpolate the concentration of the sample, by inverting the Beer-Lambert equation. 

For each measurement of the sample pigment at each wavelength, I linearly interpolate the concentration and calculate an error on each estimate. I take a weighed mean of the concentration measurements, weighting by an inverse fano-factor. Using a weighed mean I estimate the concentration of the unkown pigment to be 43.1 +/- 4.8 mg/L. Limiting the estimate to just around the central peak, where there is less uncertainty in the estimate, a the mean of the concentration estimates is 43.2 +/- 1.1 mg/L.

