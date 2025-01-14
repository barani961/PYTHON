import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(0)
num_samples = 100
heights = np.random.normal(170, 10, num_samples)
weights = np.random.normal(70, 5, num_samples)
ages = np.random.randint(20, 40, num_samples)

# Create a DataFrame
data = pd.DataFrame({'Height': heights, 'Weight': weights, 'Age': ages})

# Summary statistics
summary_stats = data.describe()
print("Summary Statistics:")
print(summary_stats)

# Scatter plot of Height vs. Weight
plt.figure(figsize=(8, 6))
plt.scatter(data['Height'], data['Weight'], c=data['Age'], cmap='viridis')
plt.colorbar(label='Age')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Scatter Plot of Height vs. Weight')
plt.grid(True)
plt.show()

# Histogram of Age distribution
plt.figure(figsize=(8, 6))
plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age Distribution')
plt.grid(True)
plt.show()
