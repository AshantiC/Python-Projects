#Strings are the sequence of characters that can be stored kin a variable enclosed in double or single quotes

# What is string formatting: to use the value of variables in our strings to print something or to generate a customized string

# Comma is generally used when we want to format a string and use the value of the variable at the end

#Example
username = input("Please enter your name:")
print("Hello",username)

# Using str.format is a new way to do string formatting. it provides the new format() method
# that we can use to do simple positional formatting
# The format() method formats the specified values and inserts them inside and the string's placeholder
# the placeholder is defined using curly brackets:{}
#Example

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, {}. You are {} years old".format(name, age))

# The placeholders can be identified using named indexes{price}, numbered indexes{0}
# or even empty placeholders {}.