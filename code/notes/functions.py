# read files + data cleaning
AUS_1 = "2021Census_G17A_AUS_AUS.csv"
AUS_2 = "2021Census_G17B_AUS_AUS.csv"

def read_AusData(file_1, file_2):
    # open file
    with open(file_1,'r') as f1, open(file_2, 'r') as f2:
        f1= f1.read().splitlines()
        f2=f2.read().splitlines()
        
        #seperate heading and number and split data in each category
        heading = f1[0].split(',')[1:] +f2[0].split(',')[1:-60]
        numbers = f1[1].split(',')[1:] +f2[1].split(',')[1:-60]
        
        # convert strings in numbers to interger
        int_numbers = [int(item) for item in numbers] 
        
        # generating dictionary for each age group
        AUS={key: None for key in ['15_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75+', 'all']}
        
        # extracting data for tuple of each age group and sex
        
        # 25-34
        age_25_34_M = tuple(int_numbers[2::10][:15]) # Male tuple
        age_25_34_F = tuple(int_numbers[2::10][17:32]) # Female tuple
        AUS['25_34']={'M':age_25_34_M, 'F':age_25_34_F} # append to dict
        
        #35-44
        age_35_44_M = tuple(int_numbers[3::10][:15]) # Male tuple
        age_35_44_F = tuple(int_numbers[3::10][17:32]) # Female tuple
        AUS['35_44']={'M':age_35_44_M, 'F':age_35_44_F} # append to dict
        
        # 45-54
        age_45_54_M = tuple(int_numbers[4::10][:15]) # Male tuple
        age_45_54_F = tuple(int_numbers[4::10][17:32]) # Female tuple
        AUS['45_54']={'M':age_45_54_M, 'F':age_45_54_F} # append to dict
        
        # 55-64
        age_55_64_M = tuple(int_numbers[5::10][:15]) # Male tuple
        age_55_64_F = tuple(int_numbers[5::10][17:32]) # Female tuple
        AUS['55_64']={'M':age_55_64_M, 'F':age_55_64_F} # append to dict
        
        # 65-74
        age_65_74_M = tuple(int_numbers[6::10][:15]) # Male tuple
        age_65_74_F = tuple(int_numbers[6::10][17:32]) # Female tuple
        AUS['65_74']={'M':age_65_74_M, 'F':age_65_74_F} # append to dict
        
        # total
        age_all_M = tuple(int_numbers[9::10][:15]) # Male tuple
        age_all_F = tuple(int_numbers[9::10][17:32]) # Female tuple
        AUS['all']={'M':age_all_M, 'F':age_all_F} # append to dict
        
        # 15-24 and 75_over
        
        # combining the data to complete the age group [ (15-19 + 20 -24) and (75-84 + 85&over)]
        age_15_24_raw = int_numbers[::10] + int_numbers[1::10]
        age_75_raw = int_numbers[7::10] + int_numbers[8::10]
        age_all = int_numbers[9::10][:15] + int_numbers[9::10][17:32]
        age_15_24 = []
        age_75 = []
        for i in range(len(age_15_24_raw)//2):
            a = age_15_24_raw[i] + age_15_24_raw[i+34]
            b = age_75_raw[i] + age_75_raw[i+34]
            age_15_24.append(a)
            age_75.append(b)
            
        # 15-24
        age_15_24_M = tuple(age_15_24[:15]) # Male tuple
        age_15_24_F = tuple(age_15_24[17:32]) # Female tuple
        AUS['15_24']={'M':age_15_24_M, 'F':age_15_24_F} # append to dict
        
        # 75 over
        age_75_M = tuple(age_75[:15]) # Male tuple
        age_75_F = tuple(age_75[17:32]) # Female tuple
        AUS['75+']={'M':age_75_M, 'F':age_75_F} # append to dict 
                
        return AUS
read_AusData(AUS_1, AUS_2)     
# calculate gini coefficient

# plot lorenz curve
# https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4

# pie chart
# https://www.tutorialspoint.com/matplotlib/matplotlib_pie_chart.htm

# bar charts
# https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm 