# Plotting the ECDF

# Youwillnowuseyourecdf()functiontocomputetheECDF for thepetallengthsof
# Anderson ecdf() function returns two arrays so you will need to unpack them.

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers, y_vers,  marker= '.', linestyle= 'none')

# Label the axes
plt.xlabel('Petal Length (cm)')
plt.ylabel('ECDF')

# Display the plot
plt.show()
