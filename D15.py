import matplotlib.pyplot as plt

# Define the range of y values
y_values = range(-5, 6)

# Calculate the square of each y value
y_squared = [y**2 for y in y_values]

# Plot the square of y values
plt.plot(y_values, y_squared, marker='o')

# Add labels and title
plt.xlabel('y')
plt.ylabel('y^2')
plt.title('Square of y over the range -5 <= y < 6')

# Display the plot
plt.grid(True)
plt.show()
