def set_intrvls (message):
  point=0
  while isinstance(point, float) == False or isinstance(point, int) == False: 
    point = input(message)
    try: 
      float(point)
      break
    except ValueError:
      try: 
        int(point)
        break
      except ValueError:
        print("Please enter a number")
  return point

def set_target_leg(message):
  value = None
  while isinstance(value, str) == False:
    value = input(message)
    is_valid_leg = value_contains(value)
    if is_valid_leg == True:
      break
    else:
      print("Enter a valid Leg")

  return value

def value_contains(item):
  item.lower().replace(" ","")
  item.lower().replace("#","")
  check_value1 = False
  if item[:2] == "leg" and type(int(item[:-1])) == int:
    check_value1 = True
  return check_value1