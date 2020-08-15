# list is unordered collection of one or more similar or dissimilar items can be stored together

simple_list = [] # An empty list with no elements

integer_list = [20, 10, 30, 40] # list of integers storing numbers
print(integer_list)
print(type(integer_list))

integer_list.sort()
print(integer_list) # Sorted in ascending order

integer_list.sort(reverse=True)
print(integer_list) # Sorted in descending order

string_list = ['apple', 'mango', 'banana'] # list of string storing names of fruits
print(string_list[1]) # We are only requesting 2nd element i.e mango - list index starts from 0

print('Number of fruits are ', len(string_list)) # Gives the number of elements in the list

string_list.append('papaya') # Add new element to the existing list
print(string_list)

string_list.remove('apple') # Remove element from list
print(string_list)

mixed_list = ['Rakesh', 30, 40651.87] # Mixed list storing name, age, salary
print("Name: {}, Age: {}, Salary: {}".format(mixed_list[0], mixed_list[1], mixed_list[2]))

alphabet_list = list('Monkey')
print(alphabet_list)