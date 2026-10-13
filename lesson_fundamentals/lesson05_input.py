# USER INPUT IN PYTHON
#print("<PROMPT>")

# name = input("Enter your name: ")
# print(f"Hello {name}")

# print(type(name))

# age = input("Enter your age: ")
# print(f"Your age is {age}")

# print(type(age))

# age_converted = int(age)

# print(type(age_converted))

# height = float(input("Enter your height: "))
# print(f"You are {height + 1} inches")


# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

favcolor = input("What is your favorite color ")
print(f"Your favorite color is {favcolor}")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))
print(f"The sum of the two number you entered is {num1+num2}")


# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 


diameter = int(input("Enter the diameter of the circle you want to calculate the area for "))
radius = diameter /2 
pi = 3.14
circlearea = 3.14 *(radius ** 2)
print(f"The area of the circle is {circlearea}")

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.
import random
sides = int(input("How many sides do you want the dice to have "))
diceroll = random.randint(1 , sides)
print(f"Here is what you rolled {diceroll}")