import pandas as pd
import numpy as np
import os

# Simulated data creation for Power BI dashboards
# 1. Team Performance Metrics
team_data = {
    "Team Member": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Active Projects": [3, 5, 2, 4, 1],
    "Tasks Overdue": [2, 1, 0, 3, 0],
    "Utilization Rate (%)": [75, 80, 60, 85, 50],
    "Average Completion Time (Days)": [25, 30, 20, 35, 15],
}

# 2. Project Status Overview
project_status_data = {
    "Project Name": ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"],
    "Status": ["In Progress", "Completed", "At Risk", "In Progress", "Completed"],
    "Due Date": ["2024-12-15", "2024-11-30", "2024-12-20", "2025-01-10", "2024-11-25"],
    "Project Lead": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
}

# 3. Data Quality Metrics
data_quality_data = {
    "Dataset Name": ["Sales Data", "Customer Data", "Inventory Data", "Finance Data"],
    "Data Completeness (%)": [95, 90, 85, 98],
    "Error Rate (%)": [5, 10, 15, 2],
    "Time to Resolve Issues (Hours)": [4, 8, 12, 3],
}

# 4. Analytics Insights Summary
analytics_insights_data = {
    "Project": ["Customer Segmentation", "Sales Forecasting", "Inventory Optimization"],
    "Insights Generated": [10, 15, 8],
    "Insights Adopted by Business": [8, 12, 6],
    "ROI (%)": [120, 150, 110],
}

# Creating dataframes
team_df = pd.DataFrame(team_data)
project_status_df = pd.DataFrame(project_status_data)
data_quality_df = pd.DataFrame(data_quality_data)
analytics_insights_df = pd.DataFrame(analytics_insights_data)

# Saving data to CSVs for Power BI file
output_dir = "/mnt/data/PowerBI_Dashboards/"
os.makedirs(output_dir, exist_ok=True)

team_df.to_csv(os.path.join(output_dir, "Team_Performance.csv"), index=False)
project_status_df.to_csv(os.path.join(output_dir, "Project_Status.csv"), index=False)
data_quality_df.to_csv(os.path.join(output_dir, "Data_Quality.csv"), index=False)
analytics_insights_df.to_csv(os.path.join(output_dir, "Analytics_Insights.csv"), index=False)

# Path to exported data
output_dir
