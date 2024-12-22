#introduction to if-Else
# An if statement is used to check whether a particular conditions is True or False
# A colon(:) is used in python to make the code more readable and to separate the different parts of expressions
# Example: create a python program that will test the voting eligibility for the presidential elections.
#age = int(input('Enter your age:'))
#if age >= 18:
    #print('Congratulations, you are eligible to vote')
    
# Else if statememt is often used with an if statement. else block will execute if the boolean 
# expression si tested by the if block evaluates to false
#if condition
#statemetns to be executed if the conditions is true
#else:
#statments to be executed if the condition is false

age = int(input('Enter your age:'))
if age>=18:
    print("Congratulations, you can vote")
else:
    print("Sorry, you are not able to vote")
    
#The for loop is typically used to iterte over a sequence like a list. Example: apple, banna, pear,orange
fruits = ("apple", "banna", "cherry")
for fruits in fruits:
    print(fruits)
    
#While loop is a loopo that is used to repeatedly execute a block of code as long as a condition is true
i = 0
while i < 5:
 print(i)
 i += 1 #increment i to avoid an infinite loop
 
 #loop control statements can control the flow of loops using breaks, continue and else
 # a break exits the loop entirely
 # a continue skips the current iteration and continues with the next iteration
 # else: executes a block of code once the lopp finishes without hitting a break statememt
 for i in range<(10):
     if i == 5:
         break#exits the loop when i equals 5
     if i % 2 == 0:
         continue#skips even numbers
     print(i)