# A arithmetic operator is a mathematical function that takes two operands and performs a calculaton on them
# addition: adds values
# subtraction: subtracts values
# multiplication: multiples values
# Division: divides values
# modudules: Divides left hand operand by right hand operand and returns the remainder
# Exponent: perfomrs exponential(power)
#Truncation or floor division: returns the division of operands where the result is the quotient
a = 5
b = 2
c = a + b
print("Addition is", c)

# Example of subtraction
num1 = 2
num2 = 5
num3 = 5 - 2 
print('Subtraction is', num3)

# Comparison operator are used for comparing values. it returns either true or false according to the conditon
#>greater than: true if the left operand is greater than the right
#< less than: true if the left operand is less than the right
# == Equal to: true if both operands are equal.
# !=Not equal to. True if operands are not equal
# >=Greater than or equal to: true if the left operand is greater than or equal to the right
# <= less than or equal to : true if the left operand is less than or equal to the right

# Comparison Example
age = 16
requiredAge = 18
print(age>requiredAge)

age = 18
requiredAge = 18
print(age==requiredAge)

# logical operator si a symbol or word used to connect two or more expressins such that the 
#value of the compound expression produced depends only on that of the original expressions
# and: returns true if both operands are true
# or: returns true if either of the operands is true
# not: return true if the operand is false
#Example
x = True
y = False
print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)

# Membership operator can be used to check whether the course is there in the user's enrolled course list
# in: returns true if the value is found in the sequence
# not in: returns true if the value is not found in the sequence
# Example
name = 'pythonx'
print('x' in name)
print('s' in name)
print('x' not in name)
