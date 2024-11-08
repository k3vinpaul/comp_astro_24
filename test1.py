import batman
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the file
df = pd.read_csv('ExoCTK_results.csv', delim_whitespace=True)

# Imprimir las columnas c1 y c2 del dataframe
print(df[['c1', 'c2']])

# Convert columns c1 and c2 to numeric, ignoring 'nan' values
df['c1'] = pd.to_numeric(df['c1'], errors='coerce')
df['c2'] = pd.to_numeric(df['c2'], errors='coerce')

# Calculate the averages, ignoring 'nan' values
c1_avg = df['c1'].mean()
c2_avg = df['c2'].mean()

print(f'Average of c1: {c1_avg}')
print(f'Average of c2: {c2_avg}')