# Variables store any kind of information .
# Make sure to use descriptive variables names. 
# Note that variables can be overwritten 

age =73
print(age)
age = 74
print(age)
password = "G00seberryPie5"
email = "mharrell@nhvweb.net"
print("Password: ", password, "\nEmail ", email)
isComplete = False
# variable name convention for booleans
isComplete = False
isEnabled = False
isAwake = True



# math conventions:

x = 3.14 
y = 8

print(x + y)

# variables are flexible. you create or update another variable, like so:
count = 10 

print(count)

countdown = count -1

print(countdown)

count = countdown

print(count)

count = count + count
    
print(count)


# Challenge 1: Rename Variables  
# Change the variable names x, y, z below to more descriptive names. 

Name = "Radia Perlman"
age = 34
Job  = "Networking Engineer"


# Challenge 2: Update Variables  
# Create a variable called 'count' with a value of 10.  
# Use another variable to increase 'count' by 5
# Print the result

count = 10 
count_up = count + 5

print(count_up)


# Challenge 3: Swap Variables  
# Given variables num = 4 and y = "hello".  
# Swap the values so that x = "hello" and y = 4. 
# Use a temporary variable.  
# Hint: You will need to create one new variable. 

num = 4 
y = "hello"
temp = 0

temp = num
num = y 
y = temp

print(num)
print(y)