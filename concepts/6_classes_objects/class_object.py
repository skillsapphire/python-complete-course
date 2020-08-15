'''Class is a blueprint and object are real life entity
class has attributes(variables) and behavior(methods)
'''
class Student:

    # class level variable
    collegeName = "5 star college"

    # instance variable
    def __init__(self, name, rollNo): # Constructor
        self.name = name
        self.rollNo = rollNo

    def showDetails(self): # Getter method
        print("College: ", __class__.collegeName)
        print("Name: {}, Age: {}".format(self.name, self.rollNo))
        print("Subjects are: ", self.subjects)

    def setSubjects(self, subjects):  # Setter method
        self.subjects = subjects

student1 = Student("Rajeev", 1221)
student1.setSubjects(['Maths', 'Physics', 'Chemistry'])
student1.showDetails()
print("Another way to get College name: ", student1.__class__.collegeName)

print('============Another Student============')

student1 = Student("Ajay", 2246)
student1.setSubjects(['Computer', 'Physics', 'Chemistry'])
student1.showDetails()
