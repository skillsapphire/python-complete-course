'''Different data types in python are
int, float, str, bool, complex
'''

var_int = 5 # Stores integer type of data
print(type(var_int))

var_str = 'I am a string value' # Stores string type of data
print(type(var_str))

var_float = 2.75 # Stores decimal type of data
print(type(var_float))

var_boolean = True # Stores boolean type of data another value could be False
print(type(var_boolean))

var_complex = 3 + 5j # Stores complex type of data
print(type(var_complex))

# We can convert one data type to another in two ways : Implicit and Explicit conversion

# Implicit conversion - automatic conversion of smaller data type to larger type
result = var_int + var_float # Implicit data type conversion example
print('Result of addition is {} and the data type of result is {}'.format(result, type(result)))

''' Explicit conversion - We convert the data type of an variable to the required data type 
by using python provided functions like int(), float(), str()'''

var_num_int = 100 # It's a number data whose value is numeric 100
print(type(var_num_int)) # Output will be int data type

var_num_str = "100" # It's a string data whose value is 100
print(type(var_num_str)) # Output will be str data type

converted_str_to_int_data = int(var_num_str) # Explicit data type conversion example
print(type(converted_str_to_int_data)) # Output will be str as the string value "100" has been converted to int value by int() function

# We could also explicitly convert the user input to any data type, because input() also returns string
var_salary = input("Enter your salary: ")

# Uncommenting below line will throw error because we are adding int 5 to an entered string value
# var_salary = var_salary + 5
print(type(var_salary)) # Output will be str

var_converted_salary = float(var_salary) # Explicitly converting entered str to float type
print(type(var_converted_salary)) # Output will be float

new_salary = var_converted_salary + 240.59 # This line will not throw error because now we are adding two float data types
print("Your new salary is", new_salary)