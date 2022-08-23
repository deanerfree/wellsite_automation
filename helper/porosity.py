import csv

def set_porosity (data_file, start_point, end_point):
  value = '4407'
  count = 0 
  item={"por0": 0, "por1": 0,"por2": 0, "por3": 0,"por4": 0, "por5": 0}
  with open(data_file, 'r') as well_data:
    well_data_reader = csv.reader(well_data, delimiter='\t')

    for well in well_data_reader:
      
      if(len(well) >= 4 and well[2] == value):

        if(float(well[0].replace(" ","")) >= float(start_point) and float(well[4]) <= float(end_point)):
          count += float(well[4])-float(well[0].replace(" ",""))
          if(well[5] == '0' or well[5] == '1'):
            item['por0'] = float(well[4])-float(well[0].replace(" ",""))+item['por0']
          if(well[5] == '2'):
            item['por1'] = float(well[4])-float(well[0].replace(" ",""))+item["por1"]
          if(well[5] == '3'):
            item['por2'] = float(well[4])-float(well[0].replace(" ",""))+item["por2"]
          if(well[5] == '4'):
            item['por3'] = float(well[4])-float(well[0].replace(" ",""))+item["por3"]
          if(well[5] == '5'):
            item['por4'] = float(well[4])-float(well[0].replace(" ",""))+item["por4"]
          if(well[5] == '6' or well[5] == '7'):
            item['por5'] = float(well[4])-float(well[0].replace(" ",""))+item["por5"]

      else:
        continue
  sumtotal = item['por0']+item['por1']+item['por2']+item['por3']+item['por4']+item['por5']
  print(sumtotal)
  return item
  