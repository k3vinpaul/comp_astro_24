import batman
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yaml


#Read the data from the txt file and create a pandas dataframe to calculate the main of the parameters c1 and c2 of the transit model
# Read the file
df = pd.read_csv('ExoCTK_results2.csv', delim_whitespace=True)

# Convert columns c1 and c2 to numeric, ignoring 'nan' values
df['c1'] = pd.to_numeric(df['c1'], errors='coerce')
df['c2'] = pd.to_numeric(df['c2'], errors='coerce')

# Calculate the averages, ignoring 'nan' values
c1_avg = df['c1'].mean()
c2_avg = df['c2'].mean()

print(f'Average of c1: {c1_avg}')
print(f'Average of c2: {c2_avg}')

#Convert the stellar radius of the star in jupiter radius
def stellar_radius(radius_star):
    radius_star_jupiter = radius_star * 0.1027 #Convert the stellar radius to jupiter radius
    return radius_star_jupiter          #Return the stellar radius in jupiter radius


#Define the parameters as in the webpages of the Exoplanet catalog
radius_planet = 0.74 #Radius of the planet in jupiter radius
stellar_rad = 1.497 #Radius of the star in solar radius

#Convert the radius of the planet in units of stellar radii
def planet_radius(radius_planet):
    radius = radius_planet * 0.1027 #Convert the planet radius to stellar radii
    return radius          #Return the planet radius in stellar radii

#Convert the Astronomical Unit to the stellar radius
def AU_to_stellar_radius(AU):
    stellar_radius = AU * 214.9394693836 #Convert the AU to the stellar radius
    return stellar_radius          #Return the stellar radius in stellar radius

#Define the semi-major axis of the planet in units of stellar radii
semi_major_axis = AU_to_stellar_radius(0.041) #Semi-major axis of the planet in units of stellar radii

#Define the parameters of the transit model using the planet TOI-2145b selected from the Exoplanet catalog
params = batman.TransitParams()
params.t0 = 0.                       #time of inferior conjunction
params.per = 2.8758916                #orbital period in days
params.rp = planet_radius(radius_planet)                    #planet radius (in units of stellar radii)
params.a = semi_major_axis                 #semi-major axis (in units of stellar radii)
params.inc = 84.1                    #orbital inclination (in degrees)
params.ecc = 0.013                    #eccentricity
params.w = 109.0                       #longitude of periastron (in degrees)
params.u = [c1_avg, c2_avg]                #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"       #limb darkening model

#Time array to calculate the transit model
t = np.linspace(-0.05 , 0.05 , 1000)

#Initialize the transit model and calculate the model light curve
m = batman.TransitModel(params, t)    #initializes model
flux = m.light_curve(params)          #calculates light curve

#Show the light curves
plt.plot(t, flux, color='blue')  # Plot the model
plt.legend("HD 149026 b")  # Add legend
plt.xlabel("Time from central transit [days] ")
plt.ylabel("Relative flux")
plt.title("HD 149026 b Light Curve")  # Add title
plt.grid(True)  # Add grid
plt.show()



# PART OF THE CHALLENGE OF THE ASSIGNMENT 1 

#def transit(params_file):
#    with open(params_file, 'r') as file:
#        params = yaml.safe_load(file)
#    
#    # Example parameters, replace with actual parameters from the YAML file
#    time = np.linspace(0, 10, 100)
#    params.get()
#    params = batman.TransitParams()
#    params.t0 = params.get("t0")                       #time of inferior conjunction
#    params.per = params.get("per")                #orbital period
#    params.rp = radius_ratio                   #planet radius (in units of stellar radii)
#    params.a = params.get("a")                    #semi-major axis (in units of stellar radii)
#    params.inc = params.get("inc")                    #orbital inclination (in degrees)
#    params.ecc = params.get("ecc")                    #eccentricity
#    params.w = params.get("w")                      #longitude of periastron (in degrees)
#    params.u = params.get("u")                #limb darkening coefficients [u1, u2]
#    params.limb_dark = "quadratic"       #limb darkening model
    
    # Simulate a simple transit light curve

    
#    plt.plot(time, light_curve)
#    plt.xlabel('Time')
#    plt.ylabel('Normalized Flux')
#    plt.title('Transit Light Curve')
#    plt.show()