import pandas as pd
import os
data = { 'Name':['Alice', 'Bob', 'Charlie', 'David'],
         'Age':[24, 27, 22, 32], 
         'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
         }

df = pd.DataFrame(data)

#Adding a new row to the DataFrame
new_row_loc = {'Name' : 'Eve', 'Age': 29, 'City': 'San Francisco'}
df.loc[len(df)] = new_row_loc



data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define file paths
file_path = os.path.join(data_dir, 'sample_data.csv')

#Save the DataFrame to a CSV file, incluidng column name
df.to_csv(file_path, index = False)

print(f"csv file saved at: {file_path}")