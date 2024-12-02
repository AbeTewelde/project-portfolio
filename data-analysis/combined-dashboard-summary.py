import pandas as pd

# Load all data
team_data = pd.read_csv("Team_Performance.csv")
project_data = pd.read_csv("Project_Status.csv")
data_quality = pd.read_csv("Data_Quality.csv")
analytics_data = pd.read_csv("Analytics_Insights.csv")

# Summary stats
team_summary = team_data.describe()
project_status_summary = project_data["Status"].value_counts()
data_quality_summary = data_quality.describe()
analytics_summary = analytics_data.describe()

# Key insights
print("Team Performance Summary:")
print(team_summary)

print("\nProject Status Summary:")
print(project_status_summary)

print("\nData Quality Summary:")
print(data_quality_summary)

print("\nAnalytics ROI Summary:")
print(analytics_summary)
