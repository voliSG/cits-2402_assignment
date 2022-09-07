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

aus_incomeBracket = [0,150,300,400,500,650,800,1000,1250,1500,1750,2000,3000,3500,4000]
														

{
  "All" : { 
            "M" : (1816370, 679812, 1005072, 1573594, 1581612, 1511161, 1438936, 1680606,
                   1866801, 1402863, 1229021, 908593, 1575067, 366363, 662715, 1486211),

            "F" : (1816370, 679812, 1005072, 1573594, 1581612, 1511161, 1438936, 1680606,
                   1866801, 1402863, 1229021, 908593, 1575067, 366363, 662715, 1486211)
          }
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

aus_income = []

#ACCESS DATA FROM SCHEMA
aus_data[age][sex]
"""