## Init income bracket (high-end)
#AUS
from decimal import *
income_AUS = [0,150,300,400,500,650,800,1000,1250,1500,1750,2000,3000,3500,4000]
aus_data = {
    '15_24': {'M': [401867, 162410, 141120, 87813, 83416,116746, 117531,
                    123463, 97720, 53244, 27805, 12952, 12892, 1989, 2709],
              'F': [336169, 192711, 166536, 107513, 92817, 117065, 108019,
                    103510, 81335, 45826, 19836, 7113, 5497, 934, 1560]},

    '25_34': {'M': [61323, 12060, 41256, 59062, 54144, 78110, 107237, 190101,
                    253148, 204733, 177553, 123848, 199901, 37621, 41765],
              'F': [130671, 30760, 64278, 80320, 88773, 144000, 164972, 200448,
                    224585, 183098, 154974, 97135, 118893, 16063, 15340]},
    
    '35_44': {'M': [43840, 9594, 31010, 44983, 41687, 52205, 68592, 124179,
                    183954, 162272, 162506, 139917, 303707, 82032, 138287],
              'F': [134456, 37076, 63660, 76485, 84778, 128803, 147445, 168374,
                    182525, 144357, 133604, 103035, 177145, 35284, 53534]},

    '45_54': {'M': [48900, 12450, 35151, 55112, 52209, 55394, 64687, 113892,
                    161923, 137540, 137333, 118911, 253897, 71957, 157499],
              'F': [114338, 33433, 59480, 84312, 90974, 122579, 135494, 160169,
                    172601, 130357, 120056, 93885, 157752, 32500, 59936]},

    '55_64': {'M': [78981, 22296, 52145, 84762, 77567, 75407, 77647, 117098,
                    155534, 118420, 110911, 88257, 166514, 44958, 97946],
              'F': [171664, 48666, 83572, 125771, 122241, 130068, 123626,
                    133267, 141177, 98151, 83348, 60947, 90648, 17873, 31538]},

    '65_74': {'M': [79097, 30627, 66614, 180976, 149579, 118233, 90066,
                    83914, 89541, 56744, 44287, 29284, 44929, 12505, 30909],
              'F': [112605, 45382, 89768, 221976, 218439, 149709, 99436,
                    74171, 60595, 34963, 26922, 17489, 22178, 5677, 12131]},

    '75+':   {'M': [43785, 18022, 49191, 186596, 147369, 91582, 66389,
                    45377, 36811, 20184, 16833, 9451, 12935, 4053, 11672],
              'F': [58682, 24314, 61287, 177914, 277604, 131263, 67809,
                    42652, 25370, 12985, 13055, 6368, 8170, 2904, 7883]},

    'all':   {'M': [757786, 267465, 416491, 699302, 605976, 587669, 592149,
                    798018, 978619, 753136, 677223, 522629, 994769, 255125, 480789],
              'F': [1058585, 412349, 588582, 874289, 975636, 923488, 846784,
                    882592, 888180, 649731, 551794, 385966, 580297, 111240, 181919]}
}

def gini(income_bracket, population):
    total_pop = sum(population)

    incomes      = []
    income_props = []
    pop_props    = []
    richer_props = []

    total_income = 0
    richer_prop = 1
    for income, pop in zip(income_bracket, population):
        sub_total_income = income * pop
        total_income += sub_total_income
        pop_prop = Decimal(pop/total_pop)

        incomes.append(sub_total_income)
        pop_props.append(pop_prop)

        richer_prop -= pop_prop
        richer_props.append(richer_prop)


    income_props = [Decimal(inc/total_income) for inc in incomes]


    score = [(income_prop * (pop_prop + 2*richer_prop))
            for income_prop, pop_prop, richer_prop in zip(income_props, pop_props, richer_props)]

    total_score = sum(score)
    gini_index = 1-total_score
    return gini_index
  
## Ranked Gini Coeffiecients by Age Group
# get gini coeffs for all age groups - call for both countries
# loop through dict
# returns dict 
#{
#  "15_24": 0.5,
#  "25_34": *gini*,
#  "35_44": ,
#  "45_54": ,
#  "55_64": ,
#  "65_74": ,
#  "75+"  : ,
#  "All"  : ,
#}
def get_gini_age(country_data, income_country):
      gini_dict_template = {}
      final_gini_dict = {}
      combined_list, gini_list = [], []
      
      #Loop through the country_data and add the corresponding element of both male and female list to make a combined population list
      for age_range in country_data:
            combined_list.append([male + female for male,female in zip(country_data[age_range]['M'], country_data[age_range]['F'])])
      #Use the gini function with each population in combined_list as its input, then make a list of gini coefficients
      for each_pop in combined_list:
            gini_coeff = gini(income_country, each_pop)
            gini_list.append(gini_coeff)
      #Create the gini template dictionary
      for age_range in country_data:
            gini_dict_template[age_range] = None
      #Assign each element from gini_list to each key in gini template dictionary
      final_gini_dict = dict(zip(gini_dict_template,gini_list))
      return final_gini_dict

print(get_gini_age(aus_data,income_AUS))