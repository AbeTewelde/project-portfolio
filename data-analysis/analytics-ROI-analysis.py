import pandas as pd
import matplotlib.pyplot as plt

# Load data
analytics_data = pd.read_csv("Analytics_Insights.csv")

# Calculate adoption rate
analytics_data["Adoption Rate (%)"] = (analytics_data["Insights Adopted by Business"] / analytics_data["Insights Generated"]) * 100

# Visualize ROI
analytics_data.plot(kind="bar", x="Project", y="ROI (%)", title="ROI by Project")
plt.show()

# Visualize adoption rate
analytics_data.plot(kind="bar", x="Project", y="Adoption Rate (%)", title="Insights Adoption Rate by Project", color="green")
plt.show()

# Display the data
print(analytics_data)
