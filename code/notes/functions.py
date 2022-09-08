# read files + data cleaning
def read_UsFile(filename):
    income_year_dict = {}
    with open(filename,'r') as data:
        content = data.read()
        lines = content.splitlines()
        for line in lines:
            #Add the all people data to the dictionary
            if "All Races" in line:
                income_people = (lines[lines.index(line)+3].split("\t")[1:-6])
                
                # replace comma and typecast strings to ints
                income_people_int = [int(num.replace(",", "")) for num in income_people]
                
                income_year_dict["All"] = income_people_int
      
            #Find the start index and end index of age data
            if "Age" in line:
                age_start = lines.index(line)+3
            if "Mean age" in line:
                age_end = lines.index(line)

        #Check if each age category is inside the file and add it to the dictionary
        for line in lines[age_start:age_end]:
            income_people = line.split("\t")[1:-6]
            
            # replace comma and typecast strings to ints
            income_people_int = [int(num.replace(",", "")) for num in income_people]

            if "15 to 24" in line:
                income_year_dict["15_24"] = income_people_int
            elif "25 to 34" in line:
                income_year_dict["25_34"] = income_people_int
            elif "35 to 44" in line:
                income_year_dict["35_44"] = income_people_int
            elif "45 to 54" in line:
                income_year_dict["45_54"] = income_people_int
            elif "55 to 64" in line:
                income_year_dict["55_64"] = income_people_int
            elif "65 to 74" in line:
                income_year_dict["65_74"] = income_people_int
            elif "75 years and over" in line:
                income_year_dict["75+"]   = income_people_int
        return income_year_dict
    

def read_UsData(filename_M, filename_F):
    final_dict =  { "15_24": {"M"  : [], "F"  : []},
                    "25_34": {"M"  : [], "F"  : []},
                    "35_44": {"M"  : [], "F"  : []},
                    "45_54": {"M"  : [], "F"  : []},
                    "55_64": {"M"  : [], "F"  : []},
                    "65_74": {"M"  : [], "F"  : []},
                    "75+"  : {"M"  : [], "F"  : []},
                    "All"  : {"M"  : [], "F"  : []},
                  }

    male_data = read_UsFile(filename_M)
    female_data = read_UsFile(filename_F)

    for (age_group,num_m), (age_group,num_f) in zip(male_data.items(), female_data.items()):
        final_dict[age_group]["M"] = num_m
        final_dict[age_group]["F"] = num_f 

    return final_dict


path       = "../../data/us/"
filename_F = path + "pinc_female.tsv"
filename_M = path + "pinc_male.tsv"

data = read_UsData(filename_M,filename_F)

for key in data:
    print(f"{key}\n{data[key]}")
# calculate gini coefficient

# plot lorenz curve
# https://gist.github.com/CMCDragonkai/c79b9a0883e31b327c88bfadb8b06fc4

# pie chart
# https://www.tutorialspoint.com/matplotlib/matplotlib_pie_chart.htm

# bar charts
# https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm 