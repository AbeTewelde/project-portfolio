import pandas as pd

# Load data
project_data = pd.read_csv("Project_Status.csv")

# Calculate project counts by status
status_counts = project_data["Status"].value_counts()

# Display status counts
print(status_counts)

# Identify at-risk projects
at_risk_projects = project_data[project_data["Status"] == "At Risk"]
print("At-Risk Projects:")
print(at_risk_projects)

# Visualize status distribution
status_counts.plot(kind="pie", autopct="%1.1f%%", title="Project Status Distribution")
plt.show()
