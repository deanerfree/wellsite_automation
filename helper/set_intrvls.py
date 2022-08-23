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