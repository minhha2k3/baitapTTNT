import numpy as np
import matplotlib.pyplot as plt

# Generate 50 evenly spaced values for x from -5 to 5
x_values = np.linspace(-5, 5, 50)

# Calculate y = x^2
y_values = x_values ** 2

# Plot (x, y)
plt.plot(x_values, y_values, label='y = x^2', color='blue')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^2')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
