my_dict = {x: x*x for x in range(0, 6)}
second_dict = {}  #new dictionary
for keys, values in my_dict.items():
  if values <= 16:
    second_dict[keys] = values
#Adding second_dict as an element of my_dict
my_dict["second_dict"] = second_dict  
for key, value in my_dict["second_dict"].items():
  print(f"{my_dict['second_dict'][key]}:{key}", end=" ")