import os
import pandas as pd

# Set the source and destination paths
source_folder = r'C:\Users\Dell XPS\Desktop\python-tools\xlsx2csv\xlsx_files'
destination_folder = r'C:\Users\Dell XPS\Desktop\python-tools\xlsx2csv\csv_files'

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through each XLSX file in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.xlsx'):
        # Construct full paths for source and destination files
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename.replace('.xlsx', '.csv'))
        
        # Load XLSX file and save as CSV
        df = pd.read_excel(source_path)
        df.to_csv(destination_path, index=False)

print("Conversion complete!")