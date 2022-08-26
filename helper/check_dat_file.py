import csv

# data_file = "input_files/rawData.dat"

def sum_porosity(por_values, well_data, value, count, start_point, end_point):
  for well in well_data:
    if(len(well) >= 4 and well[2] == value):

          if(float(well[0].replace(" ","")) >= float(start_point) and float(well[4]) <= float(end_point)):
            count += float(well[4])-float(well[0].replace(" ",""))
            if(well[5] == '0' or well[5] == '1'):
              por_values['por0'] = float(well[4])-float(well[0].replace(" ",""))+por_values['por0']
            if(well[5] == '2'):
              por_values['por1'] = float(well[4])-float(well[0].replace(" ",""))+por_values["por1"]
            if(well[5] == '3'):
              por_values['por2'] = float(well[4])-float(well[0].replace(" ",""))+por_values["por2"]
            if(well[5] == '4'):
              por_values['por3'] = float(well[4])-float(well[0].replace(" ",""))+por_values["por3"]
            if(well[5] == '5'):
              por_values['por4'] = float(well[4])-float(well[0].replace(" ",""))+por_values["por4"]
            if(well[5] == '6' or well[5] == '7'):
              por_values['por5'] = float(well[4])-float(well[0].replace(" ",""))+por_values["por5"]

    else:
      continue
  sumtotal = por_values['por0']+por_values['por1']+por_values['por2']+por_values['por3']+por_values['por4']+por_values['por5']
  print(sumtotal)
  return por_values

def set_porosity (data_file, start_point, end_point):
  target_value = '4407'
  count = 0 
  por_struct={"por0": 0, "por1": 0,"por2": 0, "por3": 0,"por4": 0, "por5": 0}
 
  with open(data_file, 'r', encoding="ISO-8859-1") as well_data:
    well_data_reader = csv.reader(well_data, delimiter='\t')
    return sum_porosity(por_struct, well_data_reader, target_value, count, start_point, end_point)
    


def check_data_exists(leg_update, data_file):
  cleanedupdata = leg_update.replace(" ", "").lower()
  target_value="SOURCE"
  with open(data_file, 'r', encoding="ISO-8859-1") as well_data:
    well_data_reader = csv.reader(well_data, delimiter='\t')

    for well in well_data_reader:
      if len(well) >= 4 and well[1] == target_value:
        file_name = well[4].replace(" ","")[:-4].lower()
        # for letter in file_name:

        target = file_name.find(cleanedupdata)
        if target:
          return True
        else:
          return False
        

