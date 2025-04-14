import pymysql
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Establish a connection to the database
connection = pymysql.connect(
    host='localhost',        # Your MySQL server address (localhost if running locally)
    user='root',             # MySQL username (root by default)
    password='Swetha@546',   # Your MySQL password
    db='healthcare_tech_db'  # The database you want to connect to
)

print("Connection successful!")

# Create a cursor object
cursor = connection.cursor()

# Query to fetch data from the technology table
query = """
SELECT tech_name, impact_area, employment_impact, success_status
FROM technology;
"""

# Execute the query
cursor.execute(query)

# Fetch all rows from the query result
data = cursor.fetchall()

# Define column names corresponding to the SELECT statement
columns = ['tech_name', 'impact_area', 'employment_impact', 'success_status']

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=columns)

# Close the cursor and connection
cursor.close()
connection.close()
#
# # Print the DataFrame to verify the data
print(df)

# cursor = connection.cursor()
#
# # Query to fetch data from the technology table
# query = """"""
# # Execute the query
# cursor.execute(query)
#
# # Fetch all rows from the query result
# data = cursor.fetchall()

# # Convert the fetched data to a pandas DataFrame
# # columns = ['tech_name', 'failure_count']

# df = pd.DataFrame(data, columns=columns)
#
# # Commit the transaction (not really needed here, but kept for consistency)
# connection.commit()
#
# # Close the connection
# cursor.close()
# connection.close()
#
# # Print the DataFrame to verify the data
# print(df)

# Group by success status
# print("\nSuccess status counts:")
# print(df['success_status'].value_counts())
#
# # Average manpower change (if it's numeric, else you may want to count occurrences)
# print("\nManpower change counts:")
# print(df['manpower_change'].value_counts())
#
# # Filter completed technologies
# completed = df[df['status'] == 'completed']
# print("\nCompleted Technologies:")
# print(completed[['tech_name', 'status']])
#
# # Technologies that were successful
# success_tech = df[df['success_status'].str.lower() == 'success']
# print("\nSuccessful Technologies:")
# print(success_tech[['tech_name', 'status']])
#
# # Technologies that failed
# failure_tech = df[df['success_status'].str.lower() == 'failure']
# print("\nFailed Technologies:")
# print(failure_tech[['tech_name', 'status']])

import matplotlib.pyplot as plt

# Count of successful and failed technologies
# status_count = df['success_status'].value_counts()
#
# plt.bar(status_count.index, status_count.values)
# plt.title('Success vs. Failure of Technologies')
# plt.xlabel('Status')
# plt.ylabel('Count')
# plt.show()


# Check column names
# print(df.columns)
#
# # If the column exists and is clean, proceed with the pie chart
# impact_area_count = df['impact_area'].value_counts()
#
# plt.pie(impact_area_count, labels=impact_area_count.index, autopct='%1.1f%%', startangle=90)
# plt.title('Distribution of Technologies by Impact Area')
# plt.show()

# manpower_change_count = df['manpower_change'].value_counts()
#
# # Stacked bar chart
# manpower_change_count.plot(kind='bar', stacked=True, color=['blue', 'orange'])
# plt.title('Manpower Change by Technology')
# plt.xlabel('Manpower Change')
# plt.ylabel('Count')
# plt.show()

# Ensure 'year' is a numeric column
# df['year'] = pd.to_numeric(df['year'], errors='coerce')

# Drop rows where 'year' is NaN
# df = df.dropna(subset=['year'])

# Count the number of technologies per year
# technologies_per_year = df['year'].value_counts().sort_index()

# Plot the data
# plt.plot(technologies_per_year.index, technologies_per_year.values)
# plt.title('Technologies Developed Over the Years')
# plt.xlabel('Year')
# plt.ylabel('Number of Technologies')
# plt.show()
#
# top_5_impact_areas = df['impact_area'].value_counts().head(5)
#
# top_5_impact_areas.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title('Top 5 Impact Areas')
# plt.xlabel('Impact Area')
# plt.ylabel('Frequency')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# Sample data (you will replace this with your actual data from SQL query)
data = {
    'tech_name': ['Telehealth', 'AI in Diagnostics', 'Wearable Health Devices', 'Blockchain for Health Data', '3D Printing for Prosthetics',
                  'Remote Patient Monitoring (RPM)', 'Genomic Medicine', 'Nanomedicine', 'AI Virtual Health Assistants', 'Robotic Surgery',
                  'EHR Systems', 'Augmented Reality (AR) in Surgery', 'Precision Medicine', 'Mobile Health Apps', 'Smart Hospitals',
                  'AI-Assisted Surgery', 'Chatbots for Mental Health', 'Cloud Healthcare Systems', 'AI for Drug Discovery', 'Digital Pathology',
                  'Cybersecurity Solutions', 'AI Radiology Assist', 'Home ICU Monitoring', 'Bio-sensors', 'Voice Recognition EHR',
                  'AI-Powered Triage', 'Digital Therapeutics', 'Electronic Prescriptions (eRx)', 'AI-Based ICU Management', 'Smart Ambulances'],
    'employment_impact': ['Decreased', 'Decreased', 'Decreased', 'Decreased', 'Decreased', 'Decreased', 'Increased', 'Increased', 'Decreased', 'Increased',
                          'Decreased', 'Increased', 'Increased', 'Decreased', 'Decreased', 'Increased', 'Decreased', 'Decreased', 'Increased', 'Increased',
                          'Increased', 'Increased', 'Increased', 'Decreased', 'Decreased', 'Increased', 'Decreased', 'Increased', 'Decreased', 'Increased']
}

df = pd.DataFrame(data)

# Filter technologies that increased employment
df_increase = df[df['employment_impact'] == 'Increased']

# Filter technologies that decreased employment
df_decrease = df[df['employment_impact'] == 'Decreased']

# Count occurrences of each category
increase_counts = df_increase['tech_name'].value_counts()
decrease_counts = df_decrease['tech_name'].value_counts()

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot the "Increased" employment technologies
plt.bar(increase_counts.index, increase_counts.values, color='green', label='Increased Employment')

# Plot the "Decreased" employment technologies
plt.bar(decrease_counts.index, decrease_counts.values, color='red', label='Decreased Employment')

plt.title('Technologies Impacting Employment')
plt.xlabel('Technology')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend()

plt.tight_layout()
plt.show()

