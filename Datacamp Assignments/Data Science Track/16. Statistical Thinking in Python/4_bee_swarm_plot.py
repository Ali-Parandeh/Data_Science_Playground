# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')

# Show the plot
plt.show()
