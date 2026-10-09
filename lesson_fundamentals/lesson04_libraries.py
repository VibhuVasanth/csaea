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

seed = 9

num = math.pow(seed, 3)
newnum = num /1
newnum2 = newnum - 0.19

print(math.ceil(newnum2))

# Bonus Challenge 
seed2 = math.ceil(newnum2)

print(seed2)

seed3 = seed2 / 38

print(seed3)

#Mr. Harrel Solution down below, study it and see how you can change your solution using this solution as a example

# seed = 45.673
# step1 = seed / 6.7
# step2 = step1 - 800
# step3 = step2 * 10
# result = math.ceil(step3)
# print("Your random num is:", result)
