"""
#DATA SCHEMA
{
  "15_24": {"M"  : (330462, 134491...),
            "F"   : (330462, 134491...)},
  "25_34": {"M"  : (330462, 134491...),
            "F"   : (330462, 134491...)},
  "35_44": {"M"  : (330462, 134491...),
            "F"   : (330462, 134491...)},
  "45_54": {"M"  : (330462, 134491...),
            "F"   : (330462, 134491...)},
  "55_64": ,
  "65_74": ,
  "75+"  : ,
  "All"  : ,
}


#FUNCTION DEFINITIONS
def read_AusData(filenames):
  pass


def read_UsFile(data, sex, filename):
  open file:
    data[age][sex].append(value) 
  return data

def read_UsData(filename_M, filename_F):
  data = {
  "15_24": {"M"  : [],
            "F"  : ()},
  "25_34": {"M"  : (),
            "F"  : ()},
  "35_44": {"M"  : (),
            "F"  : ()},
  "45_54": {"M"  : (),
            "F"  : ()},
  "55_64": {"M"  : (),
            "F"  : ()},
  "65_74": {"M"  : (),
            "F"  : ()},
  "75+"  : {"M"  : (),
            "F"  : ()},
  "All"  : {"M"  : (),
            "F"  : ()},
}
  data = read_UsFile(data, sex, filename_M)
  data = read_UsFile(data, sex, filename_F)
  return data


#FUNCTION USE CASE
aus_data = read_AusData(filenames)
us_data  = read_UsData(filename_M, filename_F)

#ACCESS DATA FROM SCHEMA
aus_data[age][]
"""