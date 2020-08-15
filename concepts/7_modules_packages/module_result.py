import module_add # File name acts as module name
from module_multiply import multiply # File name act as module name and the method from the file can be imported like this
from class_fruit import Fruit # Import a class named Fruit from a file named class_fruit

add_result = module_add.add(5, 6)
print("Result of 5 + 6 =", add_result)

multiply_result = multiply(5, 6)
print("Result of 5 * 6 =", multiply_result)

fruit = Fruit("Grapes")
print(fruit.getName())