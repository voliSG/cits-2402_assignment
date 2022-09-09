quintiles = {
    "income_prop" : [0.1, 0.15, 0.2, 0.2, 0.35], # proportion of income in quintile bracket (adds up to 1)
    "sex_prop"    : [0.6, 0.5, 0.45, 0.3, 0.25]  # proportion of males in each quintile bracket (does not add to 1)
},

# importing package
import matplotlib.pyplot as plt
import numpy as np
 
# specifying the quintiles and gender
x = ['Q1', 'Q2', 'Q3', 'Q4','Q5']
male = [sex_prop*inc_prop for sex_prop, inc_prop in zip(quintiles["sex_prop"], quintiles["income_prop"])]
female = [(1-sex_prop)*inc_prop for sex_prop, inc_prop in zip(quintiles["sex_prop"], quintiles["income_prop"])]

male_bar = np.array(male)
female_bar = np.array(female)
 
# plot the stacked bars
plt.bar(x, male_bar, color='b')
plt.bar(x, female_bar, bottom=male_bar, color='r')

plt.xlabel("Quintiles")
plt.ylabel("Gender proportion")
plt.legend(["Male", "Female"])
plt.title("Quintiles bar")
plt.show()