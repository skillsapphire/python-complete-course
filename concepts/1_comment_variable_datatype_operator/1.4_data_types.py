
var_int = 5 # Store integer type of data
print(type(var_int))
var_str = 'I am a string value' # Store string type of data
print(type(var_str))
var_float = 2.75 # Store decimal type of data
print(type(var_float))
var_boolean = True # Store boolean type of data another value could be False
print(type(var_boolean))

# We can convert one data type to another in two ways : Implicit and Explicit conversion

# Implicit conversion - automatic conversion of smaller data type to larger type
result = var_int + var_float
print('Result of addition is {} and the data type of result is {}'.format(result, type(result)))

''' Explicit conversion - We convert the data type of an variable to the required data type 
by using python provided functions like int(), float(), str()'''



