# Data transformation and cleaning
#path from notebook
path_dataFolder = "./data/aus/"
filenames_aus = ["2021Census_G17A_AUS_AUS.csv", "2021Census_G17B_AUS_AUS.csv", "2021Census_G17C_AUS_AUS.csv"]

#def read_AusData(path, filenames):
"""performs data transformation and cleaning for ABS Census data
        (G17 TOTAL PERSONAL INCOME (WEEKLY) BY AGE BY SEX)

    Args:
        filenames (list): list of filenames

    Returns:
        dictionary: 
    """

    # open file
"""
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
    """
      
def read_AusData(path, filenames):
    #comibining path to filename creating directory
    file_list=[]
    for file in filenames:
        file_list.append(path+file)
    
    #open file and sort between heading and number in each sex
    heading_M, number_M, heading_F, number_F, heading_P, number_P = [], [], [], [], [], []    
    for file in file_list:
        with open(file, 'r') as data:
            data = data.read()
            line = data.splitlines()
            head = line[0].split(',')[1:]
            num = line[1].split(',')[1:]
            for i in range(len(head)):
                # male
                if head[i].startswith('M'):
                    heading_M.append(head[i])
                    number_M.append(int(num[i]))
                # female
                if head[i].startswith('F'):
                    heading_F.append(head[i])
                    number_F.append(int(num[i]))
                # population
                if head[i].startswith('P'):
                    heading_P.append(head[i])
                    number_P.append(int(num[i]))
    
    #generating dictionary for AUS
    AUS={key: None for key in ['15_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75+', 'all']}
    
    #25-34
    age_25_34_M = number_M[2::10][:15] # Male 
    age_25_34_F = number_F[2::10][:15] # Female 
    age_25_34_P = number_P[2::10][:15] # Population
    AUS['25_34']={'M':age_25_34_M, 'F':age_25_34_F, 'P':age_25_34_P}
    
    #35-44
    age_35_44_M = number_M[3::10][:15] # Male 
    age_35_44_F = number_F[3::10][:15] # Female 
    age_35_44_P = number_P[3::10][:15] # Population
    AUS['35_44']={'M':age_35_44_M, 'F':age_35_44_F, 'P':age_35_44_P}
    
    #45-54
    age_45_54_M = number_M[4::10][:15] # Male 
    age_45_54_F = number_F[4::10][:15] # Female 
    age_45_54_P = number_P[4::10][:15] # Population
    AUS['45_54']={'M':age_45_54_M, 'F':age_45_54_F, 'P':age_45_54_P}
    
    #55-64
    age_55_64_M = number_M[5::10][:15] # Male 
    age_55_64_F = number_F[5::10][:15] # Female
    age_55_64_P = number_P[5::10][:15] # Population
    AUS['55_64']={'M':age_55_64_M, 'F':age_55_64_F, 'P':age_55_64_P}
    
    #65-74
    age_65_74_M = number_M[6::10][:15] # Male 
    age_65_74_F = number_F[6::10][:15] # Female 
    age_65_74_P = number_P[6::10][:15] # Population
    AUS['65_74']={'M':age_65_74_M, 'F':age_65_74_F, 'P':age_65_74_P}
    
    #total
    age_all_M = number_M[9::10][:15] # Male 
    age_all_F = number_F[9::10][:15] # Female 
    age_all_P = number_P[9::10][:15] # Population
    AUS['all']={'M':age_all_M, 'F':age_all_F, 'P':age_all_P}
    
     # combining the data to complete the age group [ (15-19 + 20 -24) and (75-84 + 85&over)]
    age_15_24_M = number_M[::10] + number_M[1::10]
    age_15_24_F = number_F[::10] + number_F[1::10]
    age_15_24_P = number_P[::10] + number_P[1::10]
    age_75_M = number_M[7::10] + number_M[8::10]
    age_75_F = number_F[7::10] + number_F[8::10]
    age_75_P = number_P[7::10] + number_P[8::10]
    
    age_15_24_M_f, age_15_24_F_f, age_15_24_P_f = [], [], []
    age_75_M_f, age_75_F_f, age_75_P_f = [], [], []
    
    for i in range(len(age_15_24_M)//2-2):
        age_15_24_M_f.append(age_15_24_M[i]+age_15_24_M[i+17]) # male 15-24
        age_15_24_F_f.append(age_15_24_F[i]+age_15_24_F[i+17]) # female 15-24
        age_15_24_P_f.append(age_15_24_P[i]+age_15_24_P[i+17]) # population 15-24
        age_75_M_f.append(age_75_M[i]+age_75_M[i+17]) # male 75 over
        age_75_F_f.append(age_75_F[i]+age_75_F[i+17]) # female 75 over
        age_75_P_f.append(age_75_P[i]+age_75_P[i+17]) # population 75 over
    
    # 15-24
    AUS['15_24']={'M':age_15_24_M_f, 'F':age_15_24_F_f, 'P':age_15_24_P_f} # append to dict
    # 75 over
    AUS['75+']={'M':age_75_M_f, 'F':age_75_F_f, 'P':age_75_P_f} # append to dict
    
    return AUS

print(read_AusData(path_dataFolder, filenames_aus))    