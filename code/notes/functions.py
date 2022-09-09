# read files + data cleaning

# calculate gini coefficient
def gini(income_bracket, population):
    total_pop = sum(population)
    
    incomes      = []
    income_props = []
    pop_props    = []
    richer_props = []
    
    total_income = 0
    for income, pop in zip(income_bracket, population):
        total_income += income * pop
        pop_prop = pop/total_pop

        incomes.append(income)
        pop_props.append(pop_prop)
        richer_props.append(1-pop_prop)
        
    income_props = [inc/total_income for inc in incomes]
    
    score = [income_prop * (pop_prop + 2*richer_prop)
            for income_prop, pop_prop, richer_prop in zip(income_props, pop_props, richer_props)]
    
    total_score = sum(score)
    gini_index = 1-total_score
    return gini_index
    
# get gini coeffs for all age groups - call for both countries
# loop through dict
# returns dict {age: index}

# quintile
# def quintile(income_bracket, population):
# returns list of 5 sex ratios

# plot lorenz curve
# https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4

# pie chart
# https://www.tutorialspoint.com/matplotlib/matplotlib_pie_chart.htm

# bar charts
# https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm 

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html