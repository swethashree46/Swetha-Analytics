import pymysql
import pandas as pd
import numpy as np

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Swetha@546',
    db='healthcare_tech_db'
)

print("Connection successful!")
cursor = connection.cursor()


query1 = """
SELECT tech_name, impact_area, employment_impact, success_status
FROM technology;
"""

cursor.execute(query1)
data1 = cursor.fetchall()
columns1 = ['tech_name', 'impact_area', 'employment_impact', 'success_status']
df1 = pd.DataFrame(data1, columns=columns1)

print("\nFull Technology Data:")
print(df1)

user_input = input("\nEnter an impact area to filter (e.g., 'Patient Care', 'Data security', etc.): ").strip()

query2 = """
SELECT tech_name, impact_area, employment_impact, success_status
FROM technology
WHERE impact_area = %s;
"""

cursor.execute(query2, (user_input,))
data2 = cursor.fetchall()
columns2 = ['tech_name', 'impact_area', 'employment_impact', 'success_status']
df2 = pd.DataFrame(data2, columns=columns2)

print(f"\nFiltered Data for Impact Area = '{user_input}':")
print(df2)



df2['employment_impact'] = df2['employment_impact'].str.strip().str.lower()

impact_counts = df2['employment_impact'].value_counts()

summary = {
    'Total Technologies': len(df2),
    'Increased Employment': impact_counts.get('increased', 0),
    'Decreased Employment': impact_counts.get('decreased', 0),
    'Neutral Employment': impact_counts.get('neutral', 0),  # in case it's there
    'Success Rate (%)': (df2['success_status'].str.strip().str.lower() == 'success').mean() * 100
}

# Display the summary
print("\n Analysis Summary:")
for key, value in summary.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")


try:
    year_input = int(input("\nEnter a published year (2023 - 2025): ").strip())

    if year_input < 2023 or year_input > 2025:
        print("Please enter a year between 2023 and 2025.")
    else:
        query_year = """
        SELECT tech_name, impact_area, employment_impact, success_status, year
        FROM technology
        WHERE year = %s;
        """

        cursor.execute(query_year, (year_input,))
        year_data = cursor.fetchall()

        columns = ['tech_name', 'impact_area', 'employment_impact', 'success_status', 'year']
        df_year = pd.DataFrame(year_data, columns=columns)

        if not df_year.empty:
            print(f"\nTechnologies Published in {year_input}:")
            print(df_year)


            df_year['employment_impact'] = df_year['employment_impact'].str.strip().str.lower()
            df_year['success_status'] = df_year['success_status'].str.strip().str.lower()

            # Count impact categories
            impact_counts = df_year['employment_impact'].value_counts()


            summary = {
                'Total Technologies': len(df_year),
                'Increased Employment': impact_counts.get('increased', 0),
                'Decreased Employment': impact_counts.get('decreased', 0),
                'Neutral Employment': impact_counts.get('neutral', 0),
                'Success Rate (%)': (df_year['success_status'] == 'success').mean() * 100
            }

            print("\nYear-Based Analysis:")
            for key, value in summary.items():
                print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
        else:
            print(f"\n No technologies found for year {year_input}.")

except ValueError:
    print("Invalid year. Please enter a number like 2024.")

tech_input = input("\nEnter a technology name to check its success status: ").strip()

query_status = """
SELECT tech_name, success_status
FROM technology
WHERE LOWER(tech_name) = LOWER(%s);
"""

cursor.execute(query_status, (tech_input,))
tech_status_data = cursor.fetchone()

if tech_status_data:
    tech_name, success_status = tech_status_data
    print(f"\nSuccess Status of '{tech_name}': {success_status}")
else:
    print(f"\nTechnology '{tech_input}' not found in the database.")

cursor.close()
connection.close()

