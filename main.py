import lasio
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import csv

# 4407 unique identifier for porosity
value = '4407'
data_file = "rawData.dat"
por_data =[]
item={"por0": 0, "por1": 0,"por2": 0, "por3": 0,"por4": 0, "por5": 0, "por6": 0, "por7": 0}
# print(data['HorizontalLog'])

start_point = 1040.5
end_point = 2460
count = 0 
with open(data_file, 'r') as well_data:
  well_data_reader = csv.reader(well_data, delimiter='\t')

  for well in well_data_reader:
    
    if(len(well) >= 4 and well[2] == value):

      if(float(well[0].replace(" ","")) >= start_point and float(well[4]) <= end_point):
        count += float(well[4])-float(well[0].replace(" ",""))
        if(well[5] == '0'):
          item['por0'] = float(well[4])-float(well[0].replace(" ",""))+item['por0']
        if(well[5] == '1'):
          item['por1'] = float(well[4])-float(well[0].replace(" ",""))+item["por1"]
        if(well[5] == '2'):
          item['por2'] = float(well[4])-float(well[0].replace(" ",""))+item["por2"]
        if(well[5] == '3'):
          item['por3'] = float(well[4])-float(well[0].replace(" ",""))+item["por3"]
        if(well[5] == '4'):
          item['por4'] = float(well[4])-float(well[0].replace(" ",""))+item["por4"]
        if(well[5] == '5'):
          item['por5'] = float(well[4])-float(well[0].replace(" ",""))+item["por5"]
        if(well[5] == '6'):
          item['por6'] = float(well[4])-float(well[0].replace(" ",""))+item["por6"]
        if(well[5] == '7'):
          item['por7'] = float(well[4])-float(well[0].replace(" ",""))+item["por7"]
    else:
      continue
print("Sum total: ", count)
print("Sum of each por value", item['por0']+item['por1']+item['por2']+item['por3']+item['por4']+item['por5']+item['por6']+item['por7'])
print(item)
# value = "WL_0504937_04-04-17-074-25W4-04_Leg #4 combined data curves.las"
# las = lasio.read(value)

# for item in las.well:
#   print(f"{item.descr}({item.mnemonic}):{item.value}")
#   if item.descr == "Country" and item.value == "":
#     item.value = "Canada"
#   if (item.descr == "Province       (required if CTRY = CA)" and item.value == ""):
#     item.value = "Alberta"
#   if item.descr == "Field" and item.value == "":
#     item.value = "Marten Hills (Zone 12)"
  
# las.write("WL_0504937_04-04-17-074-25W4-04_Leg #4 combined data curves fixed.las", version=2.0)
# print("file saved")
# for count, curve in enumerate(las.curves):
#   print(f"{curve.mnemonic}")