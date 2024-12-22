#this data is stored in the memory, and when we want to 'label' it as a piece of information, we call it a variable
#how do we create a varibale and store some data in python
#declare a label to the memory location-variable name
#assign the value using 'Equals'(=)-assignment operator
#give the required value-data needed to be stored
#we have an application that needs to store the names of countries
# we will define a variable for it like this
country = 'India'
#we want to pritn the value that the variable 'country' holds
#we will just pass the variable name to the print()function
print(country)

#exercise 1: create a variable and give it an assignment
name = 'Ashanti'
print(name)

# A variable is used to store any type of data that is required by the application
#that data can be a word, a number, a decimal, etc.

#Numeric Type in python consist of integer,floating point, complex
#integers are whole numbers not decimal numbers and can be either positve or negative
#floating point are numbers that can have a decimal
#complex numberis one that can be expressed in the form a +bi, where a and b are real numbers,
# and i satisifes the equation. i is called an imaginary number
number = 5 + 3j
print(number)

# A string is a sequence of characters
#Example 1: we want to store the first name and the last name of the user
firstname = 'Ashanti'
Lastname = 'Cocroft'
print(firstname)
print(Lastname)

# A multi-line string allows storing multiline strings using the 'triple quotes' syntax
quote = """Always code as if the guy who ends up maintaing your code 
will be a violent psychopath who knows where you live. 
- John Woods"""
print(quote)
#boolean is used to compare two values or work with some conditions to define it is true or false
print(2>10)
print(5<10)

# The type() function provides that return the type of object i.e the data type of variable
#Example
name = 'john'
age = 23
weight = 206.3
print(type(name))
print(type(age))
print(type(weight))

# Lets make the user do some work now
# Python provides us with the inbuilt input() function to read the user input from the keyboard
# too make it simple input allows the user to type
#Example
#input('please enter your name:')
username = input('please enter your name')
print(username)