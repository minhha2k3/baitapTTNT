import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(-5, 5, 100)  # Generating 100 points between -5 and 5

# Calculate y = exp(x)
y_values = np.exp(x_values)

# Plot y=exp(x)
plt.plot(x_values, y_values, label='$y=e^x$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y=e^x$')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
