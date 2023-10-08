import pandas as pd

# Read the first few rows of the CSV file to understand its structure
starbucks_df = pd.read_csv("starbucks.csv")
starbucks_df.head()

insert_queries = []

for index, row in starbucks_df.iterrows():
    query = f"INSERT INTO locations (title, address, gu, lat, lng) VALUES ('{row['title']}', '{row['address']}', '{row['gu']}', {row['lat']}, {row['lng']});"
    insert_queries.append(query)

# Display the first few INSERT queries for review
insert_queries