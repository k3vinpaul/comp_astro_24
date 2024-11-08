import batman
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Read the data from the txt file and create a pandas dataframe to calculate the main of the parameters c1 and c2 of the transit model
# Read the file
df = pd.read_csv('ExoCTK_results.csv', delim_whitespace=True)

# Convert columns c1 and c2 to numeric, ignoring 'nan' values
df['c1'] = pd.to_numeric(df['c1'], errors='coerce')
df['c2'] = pd.to_numeric(df['c2'], errors='coerce')

# Calculate the averages, ignoring 'nan' values
c1_avg = df['c1'].mean()
c2_avg = df['c2'].mean()

print(f'Average of c1: {c1_avg}')
print(f'Average of c2: {c2_avg}')

#Convert the units of the raduis and the other parameters to the units required by the transit model by batman package
r_planet = 1.108     #Convert the radius of the planet from Jupiter
r_star_ = 2.75        #Convert the radius of the star from Solar radii Jupiter radii
radius_ratio = r_planet/r_star_  #Calculate the radius ratio between the planet and the star, this is the parameter rp in the transit model
print(f'Radius ratio: {radius_ratio}')

#Define the parameters of the transit model using the planet TOI-2145b selected from the Exoplanet catalog
params = batman.TransitParams()
params.t0 = 0.                       #time of inferior conjunction
params.per = 10.26                #orbital period
params.rp = radius_ratio                    #planet radius (in units of stellar radii)
params.a = 8.68                     #semi-major axis (in units of stellar radii)
params.inc = 88.1                    #orbital inclination (in degrees)
params.ecc = 0.21                    #eccentricity
params.w = 96.37                       #longitude of periastron (in degrees)
params.u = [int(c1_avg), int(c2_avg)]                #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"       #limb darkening model

#Time array to calculate the transit model
t = np.linspace(-0.3 , 0.3 , 100)

#Initialize the transit model and calculate the model light curve

m = batman.TransitModel(params, t)    #initializes model
flux = m.light_curve(params)          #calculates light curve

#Show the light curves
plt.plot(t, flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.show()