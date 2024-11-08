import batman
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Read the data from the txt file and create a pandas dataframe to calculate the main of the parameters c1 and c2 of the transit model
# Read the file
file_path = 'ExoCTK_results.csv'
df = pd.read_csv(file_path, delim_whitespace=True, skiprows=2)

# Convert columns c1 and c2 to numeric, ignoring 'nan' values
df['c1'] = pd.to_numeric(df['c1'], errors='coerce')
df['c2'] = pd.to_numeric(df['c2'], errors='coerce')

# Calculate the averages, ignoring 'nan' values
c1_avg = df['c1'].mean()
c2_avg = df['c2'].mean()

print(f'Average of c1: {c1_avg}')
print(f'Average of c2: {c2_avg}')


 #Define the parameters of the transit model using the planet TOI-2145b selected from the Exoplanet catalog
params = batman.TransitParams()
params.t0 = 0.                       #time of inferior conjunction
params.per = 10.261131                #orbital period
params.rp = 1.098                    #planet radius (in units of stellar radii)
params.a = 0.11                     #semi-major axis (in units of stellar radii)
params.inc = 88.1                    #orbital inclination (in degrees)
params.ecc = 0.22                    #eccentricity
params.w = 96.37                       #longitude of periastron (in degrees)
params.u = [c1_avg, c2_avg]                #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"       #limb darkening model

#Time array to calculate the transit model
t=np.linspace(-0.05,0.05,100)

#Initialize the transit model and calculate the model light curve

m = batman.TransitModel(params, t)    #initializes model
flux = m.light_curve(params)          #calculates light curve

#Show the light curves
plt.plot(t, flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.show()