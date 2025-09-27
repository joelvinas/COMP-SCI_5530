from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np

#--Question #1--
#Stage 1: Ingest
df=pd.read_csv('sample_data/frailty_data.csv')


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

#3a:   Unit Standardization
df['Height_m'] = (df['Height_in'] * 0.0254).apply(pd.to_numeric, errors='coerce')
df['Weight_lb'] = (df['Weight_kg'] * 0.45359237).apply(pd.to_numeric, errors='coerce')

#3b:  Feature Engineering
df['BMI'] = round(df['Weight_kg'] / (df['Height_m'] ** 2),2)

def AgeGroups(Age):
  if Age < 30:
    return "<30"
  elif 30 <= Age < 45:
    return "30-45"
  elif 45 <= Age < 60:
    return "45-60"
  elif Age >= 60:
    return ">60"
  else:
    return ""

df['AgeGroup (categorical)'] = df['Age_yr'].apply(AgeGroups)

#3c.    Categorical → numeric encoding
#3ci.	  Binary encoding: Frailty_binary (Y→1, N→0, store as int8).
df['Frailty_binary'] = (df['Frailty'] =='Y').astype('int8')

#3cii.	One‑hot encode AgeGroup into columns: AgeGroup_<30, AgeGroup_30–45, AgeGroup_46–60, AgeGroup_>60
print('Help: Concept of OneHotEncode not fully understood - seek guidance')

#3d.    EDA & Reporting
#3di.   Compute summary table: mean/median/std for numeric columns; save to reports/findings.md

df_summary = df.select_dtypes(include='number')
for curSumCol in df_summary.columns:
  df_summary[curSumCol+'_mean'] = np.mean(df[curSumCol])
  df_summary[curSumCol+'_median'] = np.median(df[curSumCol])
  df_summary[curSumCol+'_std'] = np.std(df[curSumCol])
print("ToDo: save to reports/findings.md")
print("Requirement: Determine how to output to dir with online tools which don't have access to file store. Possible misreading of requirement.")
print("Help: Determine why a mark-down file was requested to output this, instead of .csv or .txt")

#3dii.  Quantify relation of strength ↔ frailty:
#        Compute correlation between Grip_kg and Frailty_binary, and report it.
correlation_matrix = np.corrcoef(df['Grip_kg'], df['Frailty_binary'])
correlation_xy = correlation_matrix[0,1]
print(f"Correlation between Grip (in kg) and Frailty: {correlation_xy}")

df_summary