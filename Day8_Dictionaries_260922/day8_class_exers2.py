# 2. Dictionary editor
# Write replace_dict_value(d, bad_val, good_val), which returns a dictionary with changed values
# The parameters of the function are the dictionary d to be processed and the values ​
# ​bad_val to be changed to good_val
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> {'a': 10, 'b': 6, 'c': 10}, 
# because 5 was the value to be replaced

original_dict = {'a': 5, 'b': 6, 'c': 5, 'd': 6}

def replace_dict_value(d, bad_val, good_val):
    for d, bad_val in original_dict.items(): 
        original_dict []# also common is k,v
print(f"{d=}, {good_val=}") # this Python 3.8+ syntax good for debugging
