from porosity import set_porosity

# 4407 unique identifier for porosity

data_file = "rawData.dat"

start_point=0
end_point=0
while isinstance(start_point, float) == False or isinstance(start_point, int) == False:  
  start_point = input("Enter the start depth: ")
  try: 
    float(start_point)
    break
  except ValueError:
    try: int(start_point)
    except ValueError:
      print("Please enter a number")

while isinstance(end_point, float) == False or isinstance(end_point, int) == False: 
  end_point = input("Enter the end depth: ")
  try: 
    float(end_point)
    break
  except ValueError:
    try: int(end_point)
    except ValueError:
      print("Please enter a number")
   
value = set_porosity(data_file, start_point, end_point)
print(value)