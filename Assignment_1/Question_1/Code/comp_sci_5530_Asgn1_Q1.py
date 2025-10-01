from sklearn.preprocessing import OneHotEncoder
import os                       #Used to manage file system
import urllib.request           #Used to obtain file from GitHub
import pandas as pd             #Used for data manipulation
import numpy as np              #Used for numerical calculations

#Question #1
#===========Stage 1: Ingestion===========
source_file_url = "https://raw.githubusercontent.com/joelvinas/COMP-SCI_5530/1111a173b9fffb6950992d13a6489c183bb7532a/Assignment_1/Question_1/Data/frailty_data.csv"
destination_path = "/tmp/frailty_data.csv" # Use a temporary path

# Download the file
try:
    urllib.request.urlretrieve(source_file_url, destination_path)
    print(f"Source File downloaded successfully to: {destination_path}")
except Exception as e:
    print(f"Error downloading source file: {e}")

df=pd.read_csv(destination_path)
#===========Stage 2: Pre-Processing===========

#Clean up field names to remove non-breaking spaces & leading/trailing spaces
for curCol in df.columns:
  df.rename(columns={curCol: curCol.replace(chr(160),chr(32)).strip()}, inplace=True)

#Clean up Frailty text
df['Frailty'] = df['Frailty'].str.strip()

#Rename columns to be embed metadata
df.rename(columns={'Height': 'Height_in', 'Weight': 'Weight_kg', 'Age': 'Age_yr'}, inplace=True)
df['Height_in'] = df['Height_in'].astype(float)
df['Weight_kg'] = df['Weight_kg'].astype(float)
df['Age_yr'] = df['Age_yr'].astype(int)
df['Grip strength'] = df['Grip strength'].astype(int)

#Rename Grip Strength
df.rename(columns={'Grip strength': 'Grip_kg'}, inplace=True)

#===========Stage 3: Analyze===========

#3a:   Unit Standardization
df['Height_m'] = (df['Height_in'] * 0.0254).apply(pd.to_numeric, errors='coerce')
df['Weight_lb'] = (df['Weight_kg'] * 0.45359237).apply(pd.to_numeric, errors='coerce')

#3b:  Feature Engineering
df['BMI'] = round(df['Weight_kg'] / (df['Height_m'] ** 2),2)

def AgeGroups(Age):
  if Age < 30:
    return "<30"
  elif 30 <= Age < 46:
    return "30-45"
  elif 46 <= Age < 61:
    return "46-60"
  elif Age > 60:
    return ">60"
  else:
    return ""

df['AgeGroup (categorical)'] = df['Age_yr'].apply(AgeGroups)

print(df)

#3c.    Categorical → numeric encoding
#3ci.     Binary encoding: Frailty_binary (Y→1, N→0, store as int8).
df['Frailty_binary'] = (df['Frailty'] =='Y').astype('int8')

#3cii.  One‑hot encode AgeGroup into columns: AgeGroup_<30, AgeGroup_30–45, AgeGroup_46–60, AgeGroup_>60
# Initialize the OneHotEncoder
# handle_unknown='ignore' prevents errors if unseen categories appear during transform
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

# Fit the encoder to the 'AgeGroup' column and transform it
# Reshape the column to a 2D array as required by OneHotEncoder
encoded_agegroups = encoder.fit_transform(df[['AgeGroup (categorical)']])

# Create a DataFrame from the encoded AgeGroups
encoded_agegroups_df = pd.DataFrame(encoded_agegroups, columns=encoder.get_feature_names_out(['AgeGroup (categorical)']))
print(encoded_agegroups_df)

#3d.    EDA & Reporting
#3di.   Compute summary table: mean/median/std for numeric columns; save to reports/findings.md

df_summary = df.select_dtypes(include='number')
summary_stats = df_summary.agg(['mean', 'median', 'std']).T
summary_stats.columns = [f'{col}_{stat}' for stat in summary_stats.columns for col in ['']]

folder_path = '/tmp/reports' # Changed directory to /tmp
file_path = folder_path + '/findings.md'
if not(os.path.isdir(folder_path)):
  os.mkdir(folder_path)

markdown_table = summary_stats.to_markdown() # Use the summary_stats DataFrame

with open(file_path, 'w') as md_file:
    md_file.write(markdown_table)

print(f"Summary table saved to: {file_path}")

#3dii.  Quantify relation of strength ↔ frailty:
#        Compute correlation between Grip_kg and Frailty_binary, and report it.
correlation_matrix = np.corrcoef(df['Grip_kg'], df['Frailty_binary'])
correlation_xy = correlation_matrix[0,1]
print(f"Correlation between Grip (in kg) and Frailty: {correlation_xy}")

#drive.flush_and_unmount()