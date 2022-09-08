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

# Australia
# getiing data for aus
data_AUS = read_AusData(path_dataFolder ,filenames_aus)
# generating size
size_sex=[]
# initializing total in male and female
total_m=0
total_f=0
count=0
# adding up all numbers in all age group for male and female
for key, value in data_AUS.items():
    if count != 7:
        for k , v in value.items():
            # male
            if k == 'M':
                for i in range(len(v)):
                    total_m += v[i]
            # female
            if k == 'F':
                for i in range(len(v)) :
                    total_f += v[i]   
        count+=1
size_sex.append(total_m)
size_sex.append(total_f)

# plotting pie chart for sex in australia
plt.pie(size_sex,labels=total_label)
plt.show()