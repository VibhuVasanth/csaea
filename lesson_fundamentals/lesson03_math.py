#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 7 + 1
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)


multiply = 8 * 1 
print("Product:", multiply )

float_divide = 22 / 7

float_divide2  = 10 /3 

print("Float Division:", float_divide)
print("Second Float Division:", float_divide2)



integer_divide = 7 // 2 
print("Integer division:", integer_divide)


mod =  7 % 2 
print("Modulus:", mod)

exponent = 7 ** 2
print("Exponent:", exponent)


#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = 2 +3 * 4
print("Result 1:", result1)

result2 = (2+3)*4

print("Result 2:", result2)


result3 = 2**3*4

print("Result 2:", result3)

result4 = 5 + 2 **3 *(4-1)

print("Result4:", result4)


# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  
# Create seperate variable, height, width, and result
height = 5
width = 8 
rectanglearea = 8*5
print("The rectangle area is:",rectanglearea)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  
radius = 7 
pi = 3.14
circlearea = pi*(radius**2)

print("The circle area:", circlearea)


# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks. 

book = 12.99
notebook = 3.50 

total = (3*book) + (4*notebook)

print(f"Book:$12.99\n Notebook: $3.50 \n The Shopping total is ${total}")


# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 
#I use the conditionals if and else.
 
num = 57

if num % 2 == 0:
    print(f"{num} is even")

else:
    print(f"{num} is odd")