from helper.check_dat_file import set_porosity
from helper.edit_geoforms import edit_geo_forms
from helper.set_intrvls import set_intrvls
import chardet

# 4407 unique identifier for porosity

data_file = "input_files/rawData.dat"
data_file2 = "input_files/raw_dat2.dat"

porosity_ss = "input_files/WL_Geoforms.xlsm"
# data =  {'por0': 92.0, 'por1': 88.5, 'por2': 371.5, 'por3': 628.0, 'por4': 305.0, 'por5': 8.5}
output_file = "output_files/demo.xlsm"

start_message = "Enter the start depth: "
end_message = "Enter the end depth: "

def check(data):
  rawdata = open(data, 'rb').read()
  result = chardet.detect(rawdata)
  charenc = result['encoding']
  print(charenc)

check(data_file2)
start_point = set_intrvls(start_message)
end_point = set_intrvls(end_message)
   
porosity_values = set_porosity(data_file2, start_point, end_point)
edit_geo_forms(porosity_ss, porosity_values, output_file)