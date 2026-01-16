'''
Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
An object is an instance of a class. It is created using the class as a template and 
can have its own unique values for the attributes defined in the class.
'''
class Car:
    '''
    The __init__ method is a special method in Python classes. 
    It is called a constructor and is automatically invoked when a new object of the class is created.

    It is used to initialize the attributes of the object with the values provided as arguments during the creation of the object.
    '''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        '''
        class attributes:
        self.make: Represents the manufacturer of the car.
        self.model: Represents the model of the car.
        self.year: Represents the year the car was manufactured.
        '''
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

car1.color = 'Red'
car2.color = 'Black'

'''
color is an object attribute added to each car object individually. This attribute is not defined in the Car class, 
which makes it an object-specific attribute.
'''
print('Car1\'s Details:')
print(f"| Year: {car1.year} | Make:  {car1.make} | Model: {car1.model} | Color: {car1.color}")


'''
Using Constructors and destructors

Constructors are special methods that are automatically called when an object of a class is created.
The purpose of a constructor is to initialize the object's attributes and allocate any necessary resources.
Eg: __init__ method in Python is a constructor that initializes the object's attributes.

Types of Constructors:
1. Default Constructor: A constructor that takes no parameters and initializes the object with default values.
Eg:
class DefaultCar:
    pass
2. Parameterized Constructor: A constructor that takes parameters to initialize the object's attributes with specific values. 
Eg:
class ParameterizedCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
3. Non-Parameterized Constructor: A constructor that does not take any parameters but initializes the object's attributes with predefined values.
Eg: 
class NonParameterizedCar:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2021
'''

'''
Destructors are special methods that are automatically called when an object is about to be destroyed or deallocated.
The purpose of a destructor is to perform any necessary cleanup tasks, such as releasing resources or closing files.
In python, the __del__ method is a destructor that is called when an object is about to be destroyed.
'''
'''
Class methods and object methods

Class methods: 
Class methods are methods that are bound to the class and not the instance of the class.
They can be called on the class itself, rather than on an instance of the class.
They are defined using the @classmethod decorator and take cls as the first parameter, which refers to the class itself.
Eg:
class MyClass:
    @classmethod
    def my_class_method(cls):
        print("This is a class method.")

Object methods:
Object methods, also known as instance methods, are methods that are bound to the instance of the class.
They can be called on the instance of the class and can access and modify the instance's attributes.
They are defined without any decorators and take self as the first parameter, which refers to the instance itself.
Eg:
class MyClass:
    def my_instance_method(self):
        print("This is an instance method.")
'''

class MyClass:
    class_attribute = "I am a class attribute"

    @classmethod
    def my_class_method(cls):
        return f"This is a class method. {cls.class_attribute}"

    def my_instance_method(self):
        return "This is an instance method."

print(MyClass.my_class_method())  # Calling class method
obj1 = MyClass()
print(obj1.my_instance_method())  # Calling instance method