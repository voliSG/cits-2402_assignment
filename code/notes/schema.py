"""
#DATA SCHEMA
{
  "15_24": {"M"  : (330462, 134491...),
            "F"   : (330462, 134491...)},
  "25_34": ,
  "35_44": ,
  "45_54": ,
  "55_64": ,
  "65_74": ,
  "75+"  : ,
  "All"  : ,
}


#FUNCTION DEFINITIONS
def read_AusData(filenames):
  pass


def read_UsFile(data, sex, filename):
  return data

def read_UsData(filename_M, filename_F):
  data = {}
  data = read_UsFile(data, sex, filename_M)
  data = read_UsFile(data, sex, filename_F)
  return data


#FUNCTION USE CASE
aus_data = read_AusData(filenames)
us_data  = read_UsData(filename_M, filename_F)

#ACCESS DATA FROM SCHEMA
aus_data[age][]
"""