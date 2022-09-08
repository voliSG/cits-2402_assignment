# Data transformation and cleaning
#path from notebook
path_dataFolder = "../data/aus/"
filenames_aus = ["2021Census_G17A_AUS_AUS.csv", "2021Census_G17B_AUS_AUS.csv", "2021Census_G17C_AUS_AUS.csv"]
      
def read_AusData(path, filenames):
    #comibining path to filename creating directory
    file_list=[]
    for file in filenames:
        file_list.append(path+file)
    
    #open file and sort between heading and number in each sex
    heading_M, number_M, heading_F, number_F = [], [], [], []
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

    
    #generating dictionary for AUS
    AUS={key: None for key in ['15_24', '25_34', '35_44', '45_54', '55_64', '65_74', '75+', 'all']}
    
    #25-34
    age_25_34_M = number_M[2::10][:15] # Male 
    age_25_34_F = number_F[2::10][:15] # Female 
    AUS['25_34']={'M':age_25_34_M, 'F':age_25_34_F}
    
    #35-44
    age_35_44_M = number_M[3::10][:15] # Male 
    age_35_44_F = number_F[3::10][:15] # Female 
    AUS['35_44']={'M':age_35_44_M, 'F':age_35_44_F}
    
    #45-54
    age_45_54_M = number_M[4::10][:15] # Male 
    age_45_54_F = number_F[4::10][:15] # Female 
    AUS['45_54']={'M':age_45_54_M, 'F':age_45_54_F}
    
    #55-64
    age_55_64_M = number_M[5::10][:15] # Male 
    age_55_64_F = number_F[5::10][:15] # Female
    AUS['55_64']={'M':age_55_64_M, 'F':age_55_64_F}
    
    #65-74
    age_65_74_M = number_M[6::10][:15] # Male 
    age_65_74_F = number_F[6::10][:15] # Female 
    AUS['65_74']={'M':age_65_74_M, 'F':age_65_74_F}
    
    #total
    age_all_M = number_M[9::10][:15] # Male 
    age_all_F = number_F[9::10][:15] # Female 
    AUS['All']={'M':age_all_M, 'F':age_all_F}
    
     # combining the data to complete the age group [ (15-19 + 20 -24) and (75-84 + 85&over)]
    age_15_24_M = number_M[::10] + number_M[1::10]
    age_15_24_F = number_F[::10] + number_F[1::10]
    age_75_M = number_M[7::10] + number_M[8::10]
    age_75_F = number_F[7::10] + number_F[8::10]
    
    age_15_24_M_f, age_15_24_F_f = [], []
    age_75_M_f, age_75_F_f = [], []
    
    for i in range(len(age_15_24_M)//2-2):
        age_15_24_M_f.append(age_15_24_M[i]+age_15_24_M[i+17]) # male 15-24
        age_15_24_F_f.append(age_15_24_F[i]+age_15_24_F[i+17]) # female 15-24
        age_75_M_f.append(age_75_M[i]+age_75_M[i+17]) # male 75 over
        age_75_F_f.append(age_75_F[i]+age_75_F[i+17]) # female 75 over
    
    # 15-24
    AUS['15_24']={'M':age_15_24_M_f, 'F':age_15_24_F_f} # append to dict
    # 75 over
    AUS['75+']={'M':age_75_M_f, 'F':age_75_F_f} # append to dict
    
    return AUS

print(read_AusData(path_dataFolder, filenames_aus))    