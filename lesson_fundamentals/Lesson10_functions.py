
# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")


say_hi() # calling the function
say_bye()
say_hi()
say_hi()
say_bye()

#Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's parameter

def express_this(e): #e is called a PARAMETER, which is a placeholder for an ARGUMENT
  return e 

expression = express_this(3 + 2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER
print(expression)



def greeter(name):
  return f"Hi{name}"

first  = greeter(" Jojo")
second = greeter(" Bizbo")
third = greeter(" Hoppy")
fourth = greeter(" Roger")

print(f"{first} , {second} , { third}  , {fourth}")




def remainder(a,b): 
    return a % b

result = remainder(10,9)
print(result)



def is_far(distance):
  if distance >= 100:
    return "Thats far"

  if distance < 100 and distance >= 20:
    return "That's not that far"

  if distance < 20:
    return "Hey that's pretty close"


#call is_far() on four different distances, and print the result

x = 250000
y = 30
z = 45
a = 65

print(is_far(x))
print(is_far(y))
print(is_far(z))
print(is_far(a))

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler() that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run

def doubler(number, times):
      num = number    
      list_1 = []

    for i in range(times):
        num = num * 2      
        list_1.append(num)
    
    return list_1

result = doubler(3, 5)
print(result)


# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp

def say_hi():
    print("Hi")

def say_bye():
    print("Bye")


say_hi() # calling the function
say_bye()
say_hi()
say_hi()
say_bye()

#Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's parameter

def express_this(e): #e is called a PARAMETER, which is a placeholder for an ARGUMENT
  return e 

expression = express_this(3 + 2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER
print(expression)



def greeter(name):
  return f"Hi{name}"

first  = greeter(" Jojo")
second = greeter(" Bizbo")
third = greeter(" Hoppy")
fourth = greeter(" Roger")

print(f"{first} , {second} , { third}  , {fourth}")




def remainder(a,b): 
    return a % b

result = remainder(10,9)
print(result)



def is_far(distance):
  if distance >= 100:
    return "Thats far"

  if distance < 100 and distance >= 20:
    return "That's not that far"

  if distance < 20:
    return "Hey that's pretty close"


#call is_far() on four different distances, and print the result

x = 250000
y = 30
z = 45
a = 65

print(is_far(x))
print(is_far(y))
print(is_far(z))
print(is_far(a))

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler() that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run

def doubler(number, times):
      num = number    
      list_1 = []

      for i in range(times):
        num = num * 2      
        list_1.append(num)
    
      return list_1

result = doubler(3, 5)
print(result)



# For Challenges 1 - 3, first write pseudocode, then solve in code.
 
# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each. 
# 1) add any two numbers return and print the result
# 2) subtract any two numbers and print the result
# 3) divide any two numbers and print the result
# 4) multiply any two numbers and print the result 




#psuedocode
#Define 4 different functions 
# Each one with a add function
#same for each one and keep moving 


def adder(a,b):
  print(a+b)
  return a+b
def subtracter(c, b):
  print(c-b)
  return c-b
def divider(e,f):
  print(e/f)
  return e/f
def multplier(g,h):
  print(g*h)
  return g*h

sum = adder(57667565657 , 756373548)
subtracter = subtracter(8639872987, 739873987)
divider = divider(7777, 9999)
multiplier = multplier(8, 6)

print(sum)
print(subtracter)
print(divider)
print(multiplier)
  

# Challenge 2
# Make a function called average that:
# 1) accepts five numbers
# 2) returns the average
# 3) print the returned value outside the function


#psudocode
#has 5 parameters
#adds them them all together 
#divide them by 5
#the print the result stored in the variable


def averager(a,b,c,d,e):
  average = a+b+c+d+e
  average = average /5

  return average

meanav = averager(1,2,3,4,5)
print(meanav)



# Challenge 3
# Make a function called is_even that:
# 1) accepts one number
# 2) prints "Even" if the number is even
# 3) prints "Odd" if the number is odd


#psuedocode 
# make the function
# One parameter
#if the the thing is divisible to 0 is even 
#vice verse is odd


def even_odd(a):
 if  a % 2 == 0:
    return "Even"

 else:
    return "Odd"

   
num = even_odd(60)
print(num)




# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function



def analyze_word(string):
  vowelCount = 0
  consnantCount = 0
  
  for letter in string:
    if  letter in "aeiou":
      vowelCount +=1 
    else:
      consnantCount +=1
  print(vowelCount)
  print(consnantCount)

  return vowelCount
  return consnantCount

word = analyze_word("Vibhu")
print(word)
