# Comparison of ECDFs

# ECDFsalsoallowyoutocomparetwo or moredistributions
# (thoughplotsgetcluttered if youhavetoomany).Here, you
# willplotECDFs for thepetallengthsofallthreeirisspecies.
# You already wrote a function to generate ECDFs so you can put it to good use!

# TooverlayallthreeECDFsonthesameplot, youcanuseplt.plot()
# threetimes, once for eachECDF.Remembertoincludemarker = '.'
# and linestyle='none' as arguments inside plt.plot().

# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)



# Plot all ECDFs on the same plot
plt.plot(x_set, y_set, marker = '.', linestyle='none')
plt.plot(x_vers, y_vers, marker = '.', linestyle='none')
plt.plot(x_virg, y_virg, marker = '.', linestyle='none')



# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()