import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x_values = np.linspace(-5, 5, 100)

# Generate y values for exp(x) and exp(2x)
y_exp_x = np.exp(x_values)
y_exp_2x = np.exp(2 * x_values)

# Generate y values for log(x) and log(2x)
# Avoiding x = 0 to prevent log(0) errors
x_values_log = np.linspace(0.01, 5, 100)
y_log_x = np.log(x_values_log)
y_log_2x = np.log(2 * x_values_log)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2)

# Plot y=exp(x) and y=exp(2x)
ax1.plot(x_values, y_exp_x, label='$y = \exp(x)$')
ax1.plot(x_values, y_exp_2x, label='$y = \exp(2x)$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Exponential Functions')
ax1.legend()

# Plot y=log(x) and y=log(2x)
ax2.plot(x_values_log, y_log_x, label='$y = \log(x)$')
ax2.plot(x_values_log, y_log_2x, label='$y = \log(2x)$')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Logarithmic Functions')
ax2.legend()

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()
