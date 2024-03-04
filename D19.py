import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(0.01, 5, 100)  # Avoiding x = 0

# Calculate y = log(x)
y_values = np.log(x_values)

# Plot y=log(x)
plt.plot(x_values, y_values, label='$y=\log(x)$')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of $y=\log(x)$')
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
