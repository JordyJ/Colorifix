import numpy as np
import pandas as pd

def raw_data_to_df(dilutions, wavelengths, absorbances, wells, names):
    # generates a dataframe from the raw data numpy arrays
    
    df = pd.DataFrame()
    
    # Flatten out and reshape the arrays
    df["Sample"] = np.repeat(names, np.shape(wavelengths))
    df["Well"] = np.repeat(wells, np.shape(wavelengths))
    df["Wavelength"] = np.tile(wavelengths, np.shape(dilutions) )
    df["Dilution"] = np.repeat(dilutions, np.shape(wavelengths))
    df["Raw Absorbance"] = np.ravel(absorbances)
    
    # Sort the dataframe by the Sample, Dilution, then Wavelength so that triplicates end up together
    df = df.sort_values(by=["Sample","Dilution","Wavelength",])
    
    return df

def import_data(filename: str):
    # Docstring:    
    
    # Check whether the file is a csv file
    if filename[-4:].lower() != '.csv':
        raise ValueError('The file is not a csv file.')
    
    # Read the csv file
    data = np.genfromtxt(filename, delimiter=',',dtype=object)
    
    # Extract the required data
    # We know that the csv files in our case have 10 rows of metadata
    wells = np.array(data[11:,0],dtype = str)
    names = np.array(data[11:,1],dtype = str)
    dilutions = np.array(data[11:,2],dtype = float)
    wavelengths = np.array(data[10,3:],dtype = float)
    absorbances = np.array(data[11:,3:],dtype = float)
    
    # Construct a pandas dataframe to store the data
    df = raw_data_to_df(dilutions, wavelengths, absorbances, wells, names)
    
    return df
