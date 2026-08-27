#Scope and LEGB rule
#L-local variable -- which can be accessed within the initialized function only
#E-Enclosing variable -- initialized in outer(parent) function can be accessed in parent and child functions
#G-Global variable -- Initialized out of the function can be accessed through out the program
#B-Built-in variable -- python provided varibles which are in built
#python scope -- Local-->Enclosing-->Global-->Built-in
x='global'
def outer():
    x='enclosive'
    def inner():
        x='Local'
        print("This is inner function x variable:",x)
    inner()
    print("This is outer function x variable:",x)
outer()
print("This is global variable x:",x)   

#A closure is a function that remembers variables from its enclosing scope even after 
#that scope has finished executing. This is the foundation of decorators, factory 
#functions, and memoisation. 

print("*"*25+'closure example'+'*'*25)
def make_multiplication(n):
    def multiply(x):
        return x*n
    return multiply

double=make_multiplication(2)
triple=make_multiplication(3)
print("Double of number 50 is:",double(50))
print("Triple of number 10 is:",triple(10))
print(double.__closure__[0].cell_contents)

print("*"*25+'real world logger function'+'*'*25)

#realworld logger function example

def make_logger(prefix):
    def logger(message):
        return f'[{prefix}]->{message}.'
    return logger
Error=make_logger("ERROR")
Info=make_logger("INFO")
print(Error("Disk full"))
print(Info("Server started"))

#lambda functions is also known as anonynimous functions 
#lambda functions are the inline functions which are defined in single line without using keywords like return
#lambda functions are the single use functions they are not meant for reusage, just a in time process completion
#lambda functions are also used as arguments for functions like sort(),filter(),
print("*"*25+'lambda function'+'*'*25)

square_lambda = lambda X:X*X
print(square_lambda(20))

print("*"*25+'map function'+'*'*25)

#map is a function that takes 2 arguments one is a function and the array 
#map iterates through the elements in the series and gives to function which performs a task
#returns the map object which is usually converted to list or tuple

numbers = [1,2,3,4,5,6,7]
squares_of_numbers=list(map(lambda x:x*x,numbers))
print("squares of numbers is:",squares_of_numbers)

print("*"*25+'filter function'+'*'*25)

#filter() function is a function which is used to filter the elements from the array or series datatype
#filter function takes 2 positional parameters one function and a iterable data

numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x:x%2==0,numbers))
print("even numbers in numbers is : ",even_numbers)

#reduce() is a function that reduces the iterable data into a single value eg:sum of all elements in a list
#reduce function takes to positional parameters 1.function that performs the task, 2.iterable datatype(tuple,list)
#reduce function returns a single value from the array
print('*'*25+" reduce function "+'*'*25)
from functools import reduce

num=[1,2,3,4,5,23,43,45,67]
result = reduce(lambda x,y:x+y,numbers)
print("sum of numbers calculated using reduce function:",result)
product=reduce(lambda x,y:x*y,numbers)
print("Product of numbers calculated using reduce function:",product)


#string methods 
#string methods are methods which are useful to manipulate the strings
#string manipilation examples are given as:
print("*"*25+' String Methods '+"*"*25)
s=" Hello World! " #string intialization
print("String s before calling string methods: /n",s)
print("String s after calling each method:/n")
print('strip()-->',s.strip())#removes white spaces from beginning and ending of the string
print('lstrip()-->',s.lstrip())#removes white spaces at starting of the string
print('rstrip()-->',s.rstrip())#removes white spaces at ending of the string
print("split()-->",s.split())#returns a list of elements that are separated by white spaces
print('upper()-->',s.upper())#converts the string into uppercase
print('lower()-->',s.lower())#converts the string into lowercase
print('title()-->',s.title())#converts the each word starting letter into uppercase
print('swapcase()-->',s.swapcase())#switches the case for each letter upper to lower and lower to upper
print('casefold()-->',s.casefold())#converts the string into lowercase but handles unicode

#search and test
#searching is to search the with in the string

print("*"*25+" search and test "+'*'*25)
text="python is a programming language"
print('startswith("python")-->',text.startswith('python'))#checks, if string starts with python returns True else False
print('endswith("language")-->',text.endswith("language"))#check, if string ends with language returns True else False
print('find("programming")-->',text.find("programming"))#finds given argument in string,present->True else->False
print('count("a")-->',text.count("a"))#counts occurances in the string
print('isalpha()-->',text.isalpha())#checks if string is alphabets returns True
print('isdigit()-->',text.isdigit())#check if the string is numbers returns True if yes
print('isalnum()-->',text.isalnum())#check if string present alphabets and strings
print('index("a")-->',text.index('a'))#returns the first index of argument given in the string
print('isspace()-->',text.isspace())#returns true if string has white spaces

#split and join of strings
print("*"*25+" splitting and joining the strings "+"*"*25)
S='python is a programming language'
print("split()-->",s.split())#splits the given string into list of words by spaces
a='1,2,3,4,5,6'
print(a,"\n split(',')-->",a.split(','))#splits words by ,
b='''this is a
 multi line
   string'''
print('splitlines()-->',b.splitlines())#splits the string line by line 
print('replace()-->',S.replace('python','c'))
print(f"This is a example of string format variables with in string a={a} , s={s}")#string format used to access variables within the string

#regular expressions
#regular expressions are used to find the patterns instead of exact raw text
# these regular expressions are useful to validate inputs finds patterns and print logs with patterns
#RE used to validate phone numbers,email,address etc which has some common patterns in them

print("*"*25+" Regular expressions "+"*"*25)
import re
text='my mobile number is 9999999999 second mobile number is 8888888888'
print("\ntext=",text)
match=re.search(r'\d+',text)#return a re.Match object hoding pattern 1st pattern found result and starting and ending index of found string 
print("Result of finding numbers in text:",match.group())#here group() is builtin method of object re.Match which returns found string
print("starting index of result in text: ",match.start())#return the start index of found string in text
print("ending index of result in text: ",match.end())#returns the ending index of found string in text 
result=re.findall(r"\d+",text)#returns the list of all found patterns in the string
print(result)
print(re.match(r'my mobile',text))#returns the re.Match object which contain found string and start,end index
print("text before replacing:",text)
res=re.sub(r'\d+','number',text)#replaces the pattern with word number and creates a new string to variable res
print("Text after replacing with the regular expression :",res)
sentence='one two three four'
print(re.split(r'[,;\s]+',sentence))#splits the text with spaces or , or ; and returns list of splitted elements
date_pattern=r'(\d{2})-(\d{2})-(\d{4})'
m=re.search(date_pattern,'28-07-2026')
print(m.group(0))#prints 1st pattern match
print(m.group(1))#prints 2nd pattern match
print(m.group(2))#prints 3rd pattern match

#comprehension in python is a method of creating new collection in short and readable format as a single line
#comprehensions in python and their types
#types of comprehensions 1.list comprehensions 2.dict comprehensions 3.set comprehensions
#List comprehension----creating the new list with the for loop logic written in list as a single line
print("*"*25+" Comprehensions "+"*"*25)

print("\n\n----------------List comprehension-----------------\n")
squares=[x**2 for x in range(1,11)] #creates a new list collection of square numbers from 1 to 10
even_numbers=[x%2==0 for x in range(1,11)]#create a new list collection of even numbers from 1 to 10
print("List comprehension squares from 1 to 10: ",squares,type(squares))
print("List comprehension of even numbers from 1 to 10",even_numbers,type(even_numbers))

#Dict comprehension--- creating the new dict with the sigle line within dict using for loop logic
print("\n\n----------------Dict comprehension-----------------\n")

prices = {'apple': 1.5, 'banana': 0.75, 'cherry': 3.0}
inverted={v:k for v,k in prices.items()} # creates a new dict collection by iterating through the prices
print("inverted dict created using dict comprehension: ",inverted,type(inverted))

#creating new set by set comprehension using single line
print("\n\n----------------set comprehension-----------------\n")
square_set ={x**2 for x in range(1,11)}#creates a new set of squares from 1 to 10
print("set of squares with set comprehension is:",square_set,type(square_set))

#File handling
#file handling in python is working with the files such that writing the data in files
#reading the information from the file
#opening the text or binary files and accessing the data in such files

with open('test_text_file.txt','r',encoding='utf-8') as f:  #opens the file in read mode,here f is a file object holding the internal file pointer(cursor) that reads the file character by character
    content=f.read()#reads the file and stores the data in the variable
    print(content)

#reading the file line by line

with open("test_text_file.txt",'r') as f:
    lines=f.readlines()
    print([line.strip() for line in lines])

#writing the content into the file
#while writing the content into the file the existing content gets overwritten because when file is opened the file object
#with internal file pointer,internal pointer points to the starting of the file which leads to overwrittening the content in the file 
#with the new content that we give
with open("test_text_file.txt",'w') as f:#opening the text file in write mode, here f is file object containing internal file pointer
    f.write("this is the text that written by the python program through file write function")#writes the given data into file
    print("The data is successfully written into the file")

#some of file methods:
# w+ write and read --creates a file if not exists can read and write operations performed
# r+ read and write --file must exist can read and write operations performed
# rb read binary -- reads binary files such as images
# wb write binary -- writes data to the binary files
# r read data -- reads data from the file
# w writes data -- writes data to the file overwrites the data if data already exists in the file

#Json file handling
#Reading the json files
import json
print("\n\n----------------Json file handling-----------------\n")
with open("student.json",'r') as f:
    data=json.load(f)
    print("This is Json file data:",data,type(data))

#json file writing

with open("student.json",'w') as f:
    student={'name':'vishnu','age':22,'university':'osmania'}
    json.dump(student,f,indent=4)
    print("data successfully written into the json file.")

#exception handling
#exception handling is a technique of handling the error that occur at runtime in python
#exception handling is useful to display user friendly error messages that easy for non tech user to understand
#we have three types of blocks to handle the exceptions they are 1.try 2.except 3.rais
#we place the error raising code in try block and we handle the error if it occurs in exception block
#raise key word in python used to raise an exception

print("*"*25+" Exception Handling "+"*"*25)
try:
    print("Try block execution starts from here:")
    result=10/0
except ZeroDivisionError as e:
    print("Cannot divide the number by 0")
finally:
    print("this is finally block always executes")

#raising an exception using raise keyword
def set_age(age):
    if not isinstance(age,int):
        raise TypeError #if non integer value passed Type error raises
    if 150>=age<=0:
        raise ValueError #if no valid age passed Value error raises
    else:
        return age
try:
    age=set_age(0)
except TypeError as e:
    print("pass integer values only as a age.")
except ValueError as e:
    print("Enter a valid age")
finally:
    print("This is a finally block")

#custom exceptions
#custom exceptions are the exception which are created using by inheriting the class exception into the class that we want to create exceptions

class AppError(Exception):
    '''Base error for the application'''
    pass

#Exception chaining
#Exception chaining is method of raising the exception within the exception useful to disply the perfect example why another exception
#occured if one occurs
try:
    number = int("abc")
except ValueError as e:
    raise TypeError("Input must be a number") from e



