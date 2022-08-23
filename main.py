from helper.porosity import set_porosity
from helper.edit_geoforms import edit_geo_forms
from helper.set_intrvls import set_intrvls

# 4407 unique identifier for porosity

data_file = "input_files/rawData.dat"

porosity_log = "input_files/WL_Geoforms.xlsm"
# data =  {'por0': 92.0, 'por1': 88.5, 'por2': 371.5, 'por3': 628.0, 'por4': 305.0, 'por5': 8.5}
output_file = "output_files/demo.xlsm"

start_message = "Enter the start depth: "
end_message = "Enter the end depth: "


start_point = set_intrvls(start_message)
end_point = set_intrvls(end_message)
   
value = set_porosity(data_file, start_point, end_point)
edit_geo_forms(porosity_log, value, output_file)