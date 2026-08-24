#Object Oriented Programming(OOPS)
#oops are useful to create user defined datatypes 
#oops are represented in classes and object format in python
#classes are the blueprints that holds the data members and data methods
#objects are the reprsentations of the class we can create multiple objects of same class
#data members of the perticular object is accessed through object
#classes are defined using keyword class
#classe name should begin with the Capital letter
print("*"*25+" class and object "+"*"*25)
class bank_account:
    '''represents a bank accound functionalities'''
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def view_balance(self):
        print("Balance is :",self.balance)
    def view_acc_no(self):
        print("Account number is:",self.acc_no)

varma=bank_account('varma',123456789101,10000)
varma.view_acc_no()
varma.view_balance()

#constructers (__init__)
#constructor is a special method that executed just after the object creation
#useful to assign the data members
#constructor in python is created by def __init__(parameters)
print("*"*25+" constructor (__init__) method "+"*"*25)
class Animal:
    def __init__(self,animal): #here __init__ method is a constructor
        self.animal=animal #animal argument assigned to self.animal data member
dog=Animal("dog") #object creation of Animal class constructor automatically executes 'dog' argument is passed to the constructor
print(dog.animal)


#Instance methods 
#Instance methods are the methods which are called by instance(objects) it takes the instance as a first parameter
#in the place of self
#there are two types of instance methods 1.accesssor method 2.mutator method
#in accessor method you access the data members using instance method it returns the data no changes were made

print("*"*25+" Instance Method as accessor method "+"*"*25)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name

varma=Person("Varma",22)
print("getting name using accessor method in instance method:",varma.get_name())

print("*"*25+" Instance Method as mutator method "+"*"*25)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def change_name(self,new_name):
        self.name=new_name
varma=Person("Varma",22)
varma.change_name("charan")
print("Name after changing :",varma.name)


#Class method
#class method can be accessd without instances(objects) we can directly call class methods through the class name
#without initializing the object of that class
#class method can be written by using the decorator @classmethod
print("*"*25+" Class method "+"*"*25)

class Math:
    @classmethod
    def add(cls,a,b):
        return a+b
    @classmethod
    def sub(cls,a,b):
        return a-b

print(Math.add(10,20))
print(Math.sub(30,10))

#static method 
#static method is a helper function for the class, need not to be create the object to use static method
#static does not have self or cls parameters 
#static method is created by using @staticmethod decorator

print("*"*25+" Class method "+"*"*25)
class Profile:
    @staticmethod
    def greet(name):
        print("Hello ",name)

Profile.greet("varma")

#Encapsulation
#Encapsulation is a method that we wrapes the data members and methods as a block using classes
#encapsulation helps in code reusability and readability
#we can access the methods from the class
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age= age
        self.marks=marks
    def view_student(self):
        print(f"name:{self.name} , age:{self.age}, marks:{self.marks}")

varma=Student("varma",22,120)
varma.view_student()
#here in above example all the data members and methods are enclosed in a class this process is called encapsulation
#we can protect the data members which we can define the scope such that data members are 
#restricted for outside of the class by naming conversions
# we have access levels as 1)public 2)private 3)protected
# by using public we can access the data members from anywhere of the program
# by private we cannot access data member directly outside of the class
# by protected we only access the data member within class cannot be accessed out side of class

class Student:
    def __init__(self,name,age,marks):
        self.name=name #it is a public data member
        self._age=age #it is a protected data member initialized by _
        self.__marks=marks # it is the privete data member can only be accessed through the instance

    def get_marks(self):
        print("This is the private data member marks of class Student:",self.__marks)

varma=Student("Varma",22,1200)
print("This is a public data member of Student class name: ",varma.name)
print("This is a protected variable from the class Student age :",varma._age)
varma.get_marks()#the private data member can only be used by its class method
#Here python doesnt providing the security here it simpling changing the name of private data member so its preventing
#the accessing of the variable outside the class method, the process is done by name mangling which converts the 
#data member name just a name conversion, the private data member in above example self.__marks are converted
#into _Student__marks it makes the developer not to accidentlly access or modifies the private data members
#the private datamember still can be accessed outside the class method by varma._Student__marks


#Inheritance is the technique where we use the another class methods in a class by inheriting the class 
#where we have parent and child classes we can use and access the parent class properties in child class
#In inheritance we have 4 types 1)single inheritance 2)multi inheritance 3)hirarichal inheritance 4)multilevel inheritance 5)hibrid inheritance
#singe inheritance
#In sigle inheritance just one class is inherited into another class

print("*"*25+"Single Inheritance "+"*"*25)
class Animal: #Animal class
    def eating(self):
        return "Animal can eat."
class Dog(Animal):#Animal class inherited into class dog, Animal is parent class while dog is child class
    def bark(self):
        return "Dog is barking"

dog1=Dog()
print("Animal method from Dog class object:",dog1.eating())
print("Dog class method :",dog1.bark())

#multiple inhertance 
#in multiple inheritance two or more classes inherited into a single class 
print("*"*25+"Multiple Inheritance "+"*"*25)
class Eating:
    def eating(self):
        return "Animal can eat"
class Sleeping:
    def sleeping(self):
        return "Animal can slee"
class Animal(Eating,Sleeping):
    def drinking(self):
        return "Animal can drink water"

dog=Animal()
print("eating method with Animal class instance: ",dog.eating())
print("Sleep method with Animal class instance: ",dog.sleeping())
print("drinking method from Animal class instance: ",dog.drinking())

#Hirarchical inheritance 
#in Hirarchical inheritance one class is in herited into multiple classes
print("*"*25+" Hirarchical Inheritance "+"*"*25)
class Animal:
    def eat(self):
        return 'Animal can eat'
    def sleep(self):
        return 'Animal can sleep'
    def drink(self):
        return 'Animal can drink water'

class Dog(Animal): #Animal class inherited into Dog
    def bark(self):
        return 'Dog can bark'
class Lion(Animal): #Animal class inherited into Lion
    def roar(self):
        return 'Lion can Roar'
dog=Dog()
lion=Lion()
print("Dog class methods extend Animal:")
print(dog.eat())
print(dog.sleep())
print(dog.drink())
print(dog.bark())
print("Lion class methods extend Animal")
print(lion.eat())
print(lion.sleep())
print(lion.drink())
print(lion.roar())


#Multilevel Inheritance
#parent class inherited into child class and child class inherited into grand child class
print("*"*25+" Multi-level Inheritance "+"*"*25)
class Eat:
    def eat(self):
        return 'Animal can eat'
class Sleep(Eat):
    def sleep(self):
        return 'Animal can sleep'
class Dog(Sleep):
    def bark(self):
        return 'dog can bark'

dog=Dog()
print("Dog multilevel inherited class methods:")
print(dog.eat())
print(dog.sleep())
print(dog.bark())


#Hibrid Inheritance
#in Hibrid Inheritance two or more types of inheritance implimented at once
print("*"*25+" Hibrid Inheritance "+"*"*25)
class Eat:
    def eat(self):
        return 'Animal can eat'
class Sleep:
    def sleep(self):
        return 'Animal can sleep'
class Animal(Eat,Sleep):
    def drink(self):
        return 'Animal can drink water'
class Dog(Animal):
    def bark(self):
        return 'dog can bark'

dog=Dog()
print("Hibrid inheritance exmaples with Dog class:")
print(dog.eat())
print(dog.sleep())
print(dog.drink())
print(dog.bark())


#super() function
#super() is a built in function used to access the parent class methods in inherited child class
print("*"*25+" super() function "+"*"*25)
class Parent:
    def process(self):
        print("This is a parent process")
class Child(Parent):
    def process(self):
        super().process() #accessing the parent class process method
        print("This is a child Process")

s=Child()
s.process()


#Method Resolution Order(MRO)
#MRO keeps the methods order of Inherited classes
#if we access the methods through object instance python MRO first refers to the child class if not found in child
#class then searches for methods in parent classes

class Flyable:
    def move(self):
        return 'flying'
class Swimmable:
    def move(self):
        return 'swimming'
class Duck(Swimmable,Flyable):
    pass
duck=Duck()
print(duck.move())
print("The MRO structure of class object duck is: ",Duck.__mro__)


#Polimorphism 
#Polimorphism means many forms in which same methods or datamembers behave differently for different objects
#Polimorphism can be achieved by method overriding and operator overloading 
print("*"*25+" Polymorphism "+"*"*25)
class Dog:
    def speak(self):
        return 'bark'
class Animal(Dog):
    def speak(self):
        return 'Animal Sound'

dog=Dog()
animal=Animal()
print(animal.speak())
print(dog.speak())

class Employee:
    def profile(self,name):
            return f'name={name}'

class Student(Employee):
    def profile(self,name,age,marks):
        return f'name={name}, age={age}, marks={marks}'
student1=Student()
employee=Employee()
print(employee.profile("Varma"))
print(student1.profile("varma",22,100))

#Decorators is a function thats adds on or modifies the behaviour of another function 
#Decorator function takes a function as a arguement and changes the behaviour of the function it took
print("*"*25+" Decorators "+"*"*25)
def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decorator
def greet():
    print("Hello")
greet()

#decorators arguments
#decorators can recieve the arguments but to impliment decorators arguments we need 3 nested functions
#1)decorator function recieves decorator arguments 2)wrapper function/actual decorator function recieves function
#  3)function recives function arguments

print("*"*25+" Decorators arguments "+"*"*25)
def repeate(n):
    def decorator(func):
        def wrapper():
            print("Before")
            func()
            print("After")
        return wrapper
    return decorator

@repeate(3)
def greet():
    print("Hello")
greet()

#Class-Based Decorators
#A class-based decorator is a class that acts as a decorator instead of a function.
#The class must implement the __call__() method.
#When the decorated function is called, Python automatically invokes __call__().
print("*"*25+" Class Based Decorators "+"*"*25)
class Decorator:
    def __init__(self,func):
        self.func=func
    def __call__(self):
        print("Before")
        self.func()
        print("After")

@Decorator
def greet():
    print("hello")
greet()

#@property decorator
#@property decorators converts the method into a only accessable method read only method
#@property decorator is a built in python decorator
print("*"*25+" property decorator "+"*"*25)
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self._marks=marks

    @property #decorator makes the method marks only to readable method cannot manipulate the data members
    def marks(self):
        return self._marks

s1=Student("varun",22,120)
print(s1.marks)

#@property.setter this decorator used to modify the values or setting the values
#while @property makes the method only to accessable
class Student:
    def __init__(self,marks):
        self._marks=marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        self._marks=value

s2=Student(210)
print(s2.marks)
s2.marks=200
print(s2.marks)

#dunder methods (magic methods)
#Dunder means Double UNDERSCORE (__).
#Also called Magic Methods or Special Methods.
#Have the form __method__.
#Python calls them automatically for built-in operations.
#Used to customize the behavior of objects.
#__init__()	Constructor (initialize object)
#__new__()	Create object before __init__()
#__str__()	String representation for users (print())
#__repr__()	Official string representation (developers)
#__len__()	Called by len()
#__call__()	Makes an object callable like a function
#__del__()	Destructor (called before object destruction)
print("*"*25+" Common Dunder Methods "+"*"*25)

class Student:
    def __init__(self, name, marks):
        print("__init__() called")
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    def __len__(self):
        return len(self.name)

    def __call__(self):
        print(f"{self.name} object is called like a function!")

    def __add__(self, other):
        return self.marks + other.marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __del__(self):
        print(f"{self.name} object destroyed")


# Creating objects
s1 = Student("Varma", 90)
s2 = Student("Rahul", 85)

# __str__()
print(s1)

# __repr__()
print(repr(s1))

# __len__()
print("Length of name:", len(s1))

# __call__()
s1()

# __add__()
print("Total Marks:", s1 + s2)

# __eq__()
print("Equal Marks:", s1 == s2)

# __lt__()
print("s1 < s2:", s1 < s2)

# __gt__()
print("s1 > s2:", s1 > s2)

# __del__()
del s1
del s2
