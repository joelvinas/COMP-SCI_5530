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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Question #2
q2df=pd.read_csv('sample_data/StudentsPerformance.csv')


#Gender boxplots (math vs reading) (2 pts)
#a.	Question: Are there gender differences in math vs reading?
#b.	Chart: Side‑by‑side boxplots of math score and reading score grouped by gender

#First, separate the data into male/female data frames
pop_male = q2df[q2df['gender'] =='male']
pop_female = q2df[q2df['gender'] =='female']

#Box plot is obtained by using the first quartile (Q1) to the third quartile (Q3) of the data, with a line at the median
#   Source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html

#Organize data for the math score
math_scores_male = pop_male['math score']
math_scores_female = pop_female['math score']
mathdata_multiple = [math_scores_male, math_scores_female]

#Organize data for the reading score
read_scores_male = pop_male['reading score']
read_scores_female = pop_female['reading score']
readdata_multiple = [read_scores_male, read_scores_female]

#Create a figure with two subplots (1 row, 2 columns)
dpi = 300
width = 800/dpi
height = 600/dpi
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(width,height), dpi=300)
 #, dpi=300)

#Plot the Math box plot on ax1
ax1.boxplot(mathdata_multiple)
ax1.set_title('Math Scores by Gender')
ax1.set_ylabel('Math Score')
ax1.set_xticklabels(['Male', 'Female'])

#Plot the Reading box plot on ax2
ax2.boxplot(readdata_multiple)
ax2.set_title('Reading Scores by Gender')
ax2.set_ylabel('Reading Score')

ax2.set_xticklabels(['Male', 'Female'])

JVinasComment = "JVinas Note: The data shows that for math, males score higher than females. This trend is reversed when it comes to reading scores."
text = fig.text(0.5, 0, JVinasComment, horizontalalignment='center', wrap=True, font = {'size':3})

plt.tight_layout()  #Use the tight layout to prevent overlapping titles/labels
plt.rcParams.update({'font.size': 5})
plt.show()

#B.	V2 — Test prep impact on math (2 pts)
#a.	Question: Do students who completed test prep score higher in math?
#b.	Chart: Any chart of your choice for math score by test preparation course (completed vs none).

#C: Visualization #3 - Lunch type and average performance (2 pts)
#Ca.	Question: Does lunch type (standard vs free/reduced) relate to outcomes?
#Cb.	Chart: Grouped bar chart of mean overall_avg of all the scores (math, reading, writing) by lunch.

std_lunch = q2df[q2df['lunch'] =='standard']
free_lunch = q2df[q2df['lunch'] =='free/reduced']

labels = ['Free/Reduced Lunch', 'Standard Lunch']
mathing_means = [free_lunch['math score'].mean(),std_lunch['math score'].mean(),] 
reading_means = [free_lunch['reading score'].mean(),std_lunch['reading score'].mean(),]
writing_means = [free_lunch['writing score'].mean(),std_lunch['writing score'].mean()]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

dpi = 300
figwidth = 800/dpi
figheight = 600/dpi
fig, ax = plt.subplots(figsize=(figwidth,figheight), dpi=300)
rects1 = ax.bar(x - width, mathing_means, width, label='Math')
rects2 = ax.bar(x, reading_means, width, label='Reading')
rects3 = ax.bar(x + width, writing_means, width, label='Writing')

JVinasComment = "JVinas Note: \nIt appears that lunch type is related to average score. \nAs lunch type is an indicator of financial resources of the student's home, there might be underlying factors."
text = fig.text(0.45, 0.25, JVinasComment, horizontalalignment='left', wrap=True, bbox=dict(boxstyle='square,pad=0.5', fc='lightblue', ec='blue'))

ax.set_ylabel('Scores')
ax.set_title('Average Test Performance by Lunch Type')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()


#D.	V4 — Subject correlations (2 pts)
#a.	Question: How strongly do the three subjects move together?
#b.	Chart: Correlation heatmap for math, reading, writing with annotated coefficients.
#E.	V5 — Math vs reading with trend lines by test prep (2 pts)
#a.	Question: How strongly are math and reading scores associated, and do students who completed the test‑preparation course have a different slope in the math–reading relationship than those who did not?
#b.	Chart: Scatter plot with two straight best‑fit lines (one for each group: completed, none).
#i.	X‑axis: reading score 
#ii.	Y‑axis: math score
#c.	Color: Points colored by test preparation course (legend must show the two groups and each group’s n).
