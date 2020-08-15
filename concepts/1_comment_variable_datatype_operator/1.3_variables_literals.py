# Variables are placeholders in RAM memory, they can store values of a type
simpleVariable = "I am a simple variable who will store string data"
print(simpleVariable)

intVariable = 25 # I am a variable who will store single integer value
print(intVariable)

intVariable = 20 # The value that I store can be modified that's I am called variable
print(intVariable)

"""In python we do not need to specify the data type of a variable, 
python on runtime decides the data type of a variable based on the value it will store"""
testVar = 10 # Here the value 10 is numeric literal
print("Value of testVar is integer: ", testVar)

print(type(testVar)) # Using the type function you can find my data type, now i will be of type int

testVar = "My value is getting changed from int to string so now python will my data type to string"
print(testVar)

print(type(testVar)) # Using the type function you can find my data type, now i will be of type str