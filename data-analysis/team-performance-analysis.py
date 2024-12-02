import pandas as pd
import matplotlib.pyplot as plt

# Load data
team_data = pd.read_csv("Team_Performance.csv")

# Calculate summary statistics
summary = team_data.describe()

# Visualize workload distribution
team_data.plot(kind="bar", x="Team Member", y="Active Projects", title="Workload Distribution")
plt.show()

# Visualize utilization rate
team_data.plot(kind="line", x="Team Member", y="Utilization Rate (%)", title="Utilization Rate by Team Member")
plt.show()

# Overdue tasks distribution
team_data.plot(kind="bar", x="Team Member", y="Tasks Overdue", title="Overdue Tasks by Team Member")
plt.show()

print(summary)
