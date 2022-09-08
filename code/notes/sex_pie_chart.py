#Import all modules 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#Assign the first data of all male dict and all female dict to the total male and female
total_male_US, total_female_US = us_data['all']['M'][0], us_data['all']['F'][0]

#specify the label and content
total_label = ['Total male', 'Total female']
total_US_list = [total_male_US, total_female_US]

#plot the pie chart
plt.pie(total_US_list, labels=total_label)
plt.title("Gender proportion in US")

plt.show()
