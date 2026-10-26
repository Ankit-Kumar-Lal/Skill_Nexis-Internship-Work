# Use Matplotlib to Plot a Line Graph

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [28, 30, 29, 32, 31, 34, 33]

# Create the line graph
plt.plot(
    days,
    temperature,
    marker="o",
    linestyle="-",
    label="Temperature"
)

# Add title and labels
plt.title("Weekly Temperature Analysis")
plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.legend()
plt.tight_layout()

# Display the graph
plt.show()
