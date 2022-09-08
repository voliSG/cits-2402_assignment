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

# Australia
# getiing data for aus
data_AUS = read_AusData(path_dataFolder, filenames_aus)

# generating size
size_age=[]

# adding up all value in each age group
for key, value in data_AUS.items():
    total_age=0
    for k , v in value.items():
        for i in range(len(v)):
            total_age +=v[i]
    size_age.append(total_age)

# plotting pie chart
plt.pie(size_age[:-1],labels=age_label)
plt.title("Proportion of different age ranges in Australia")
plt.show()

# plot US and Australia side by side
fig, (us,aus) = plt.subplots(1,2,figsize=(10,10))

us.pie(total_age_range[:-1], labels=age_label)
us.title("Proportion of different age ranges in US")

aus.pie(size_age[:-1],labels=age_label)
aus.title("Proportion of different age ranges in Australia")

plt.show()