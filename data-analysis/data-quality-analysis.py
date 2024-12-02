import pandas as pd
import matplotlib.pyplot as plt

# Load data
data_quality = pd.read_csv("Data_Quality.csv")

# Summary statistics
summary = data_quality.describe()

# Visualize data completeness
data_quality.plot(kind="bar", x="Dataset Name", y="Data Completeness (%)", title="Data Completeness by Dataset")
plt.show()

# Visualize error rates
data_quality.plot(kind="bar", x="Dataset Name", y="Error Rate (%)", title="Error Rate by Dataset", color="red")
plt.show()

# Time to resolve issues
data_quality.plot(kind="bar", x="Dataset Name", y="Time to Resolve Issues (Hours)", title="Resolution Time by Dataset")
plt.show()

print(summary)
