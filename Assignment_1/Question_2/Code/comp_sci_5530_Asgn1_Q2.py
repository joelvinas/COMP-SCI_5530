import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Question #2
#Stage 1: Ingestion
#       ToDo: Determine how to manage source data file through both CoLab vs GitHub Repo
q2df=pd.read_csv('sample_data/StudentsPerformance.csv')

#Stage 2: Pre-Processing
#       ToDo: Use the pre-processing steps in the earlier Question to relabel columns and use proper data types.
#       Note: As the data is fairly clean, we can proceed working through learning how to create visualizations with Python
#               We can add this step later, as it should be quite easy.


#A.	V1 — Gender boxplots (math vs reading) (2 pts)
#a.	Question: Are there gender differences in math vs reading?
#b.	Chart: Side‑by‑side boxplots of math score and reading score grouped by gender.

#ToDo: Grouped by Gender, or Filtered by Gender? A box plot uses min/max/mean to showcase the distribution. Aggregation doesn't seem right.

pop_male = q2df[q2df['gender'] =='male']
pop_female = q2df[q2df['gender'] =='female']

math_score = q2df['math score']
reading_score = q2df['reading score']

pop_male_math = pop_male['math score']
pop_male_read = pop_male['reading_score']
mvr_male = [pop_male_math, pop_male_read]   #Debug: Why is this not working?
#mvr_female = [pop_female['math score'],pop_female['reading_score']]
#plt.boxplot(mvr_male)

#plt.boxplot(mathVreading)
#data_multiple = [data_1, data_2]

#plt.boxplot(data) # For a single boxplot
    # Or for multiple boxplots:
#plt.boxplot(data_multiple)

#B.	V2 — Test prep impact on math (2 pts)
#a.	Question: Do students who completed test prep score higher in math?
#b.	Chart: Any chart of your choice for math score by test preparation course (completed vs none).
#C.	V3 — Lunch type and average performance (2 pts)
#a.	Question: Does lunch type (standard vs free/reduced) relate to outcomes?
#b.	Chart: Grouped bar chart of mean overall_avg of all the scores (math, reading, writing) by lunch.
#D.	V4 — Subject correlations (2 pts)
#a.	Question: How strongly do the three subjects move together?
#b.	Chart: Correlation heatmap for math, reading, writing with annotated coefficients.
#E.	V5 — Math vs reading with trend lines by test prep (2 pts)
#a.	Question: How strongly are math and reading scores associated, and do students who completed the test‑preparation course have a different slope in the math–reading relationship than those who did not?
#b.	Chart: Scatter plot with two straight best‑fit lines (one for each group: completed, none).
#i.	X‑axis: reading score 
#ii.	Y‑axis: math score
#c.	Color: Points colored by test preparation course (legend must show the two groups and each group’s n).
