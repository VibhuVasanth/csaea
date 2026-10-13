import math 


# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html
#to bring a library you need to use the keyword import and the actual name of the library itself


sq_root = math.sqrt(25)

print("Square Root:", sq_root)


round_up = math.ceil(4.5)
print("Round  up:", round_up)


round_down = math.floor(4.8)
print(f"Round Down:{round_down}")


exponent = math.pow(2, 5)
print(exponent)


#Constants
# Constants are variables that NEVER change. They are written i all CAPS

PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2
diameter = 14 

radius = diameter/ 2 

circle_area = math.pow(radius, 2)*PI

print("The area of the circle is", circle_area)



# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator
# seed = 7  

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 
import math
seed = 123.45

num = seed + 543.21
newnum = num -99.1
newnum2 = newnum / 7.3

print(math.ceil(newnum2))

# Bonus Challenge 
seed2 = (newnum2 % 10 ) +1
seed3 = math.ceil(seed2)

print(seed3)



#Mr. Harrel Solution down below, study it and see how you can change your solution using this solution as a example

# seed = 45.673
# step1 = seed / 6.7
# step2 = step1 - 800
# step3 = step2 * 10
# result = math.ceil(step3)
# print("Your random num is:", result)


import random 


random_integer = random.randint(1,100)
print(random_integer)


random_float = random.random()
print(random_float)


my_list = ["taco", "burrito", "enchilada", "quesadilla"]

random_selection = random.choice(my_list)

print(random_selection)

random.shuffle(my_list)

print(my_list)


# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it with a message.

numbers = random. randint(1, 6)

die_roll = numbers

print(f"The number rolled is {die_roll}")


# Challenge 3: Random Square Root
# Use random library to pick a number between 1 and 75. Store it in "num".
# Use math library to find its square root.
# Print the number, its square root, and the square root rounded UP with the math library.

num = random.randint ( 1 , 75 )

num2 = math.sqrt(num)

num3 = math.ceil(num2)

print(f"The  number is {num}, and the square root of it is {num2} and the rounded up number is {num3}")

# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base," one is the "exponent."
# Use math library to raise the base to the exponent. (ie, based to the PoWer of exponent)
# Print both rolls and the result as an integer (hint: int() removes the .0).

dice1 = random.randint(1 , 6)

dice2 = random.randint(1 , 6)

num = math.pow(dice1, dice2 )

intnum = int(num)

print(f"The first dice rolled {dice1} the second dice rolled {dice2} and the integer exponent is {intnum}")