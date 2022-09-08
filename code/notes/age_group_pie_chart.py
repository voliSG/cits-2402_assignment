#Import all modules 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#Loop through the age range and add the total to total_age_range
total_age_range = []
for age in us_data:
    total_age_range.append(us_data[age]['M'][0] + us_data[age]['F'][0])
#Specify the label
age_label = ['15 to 24 years', ' 25 to 34 years','35 to 44 years','45 to 54 years','55 to 64 years','65 to 74 years', '75 years and over']

#plot
plt.pie(total_age_range[:-1], labels=age_label)
plt.title("Proportion of different age ranges in US")

plt.show()