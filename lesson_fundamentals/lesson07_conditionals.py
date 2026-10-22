# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else


# Boolean Referesher _
print(3==2)
print("Hello" ==  "Hi there")
print(7 != 4)
print(4 > 5)

# if 
num =  12
if num == 10: #only runs if condition is true
    print("Your num is equal to 10")
    print(10 + num)

#if else 

num = 5

if num <= 12:
    print("Your num is less than or equal to 12 ")
else:
    print("Your num if greater than or equal to 12")


#if, elif, else
temprature = 1

if temprature > 95:
    print("It's hot")
elif temprature >= 60:
    print("It's nice ")
elif temprature <= 0: 
    print("It freezing")
else:
    print("It's cold")


print()

x = 20
y = 20 

if x == y:
    print("The two variables are equal")

elif x > y:
    print("x is greater than y")

elif x< y : 
    print("x is greater than y ")
else: 
    print("Error. ")



# Logical operators: and 
# Both sides of the 'and' must  be true, otherwise it's false. 
age = 8
has_permission = True

if age >= 16 and has_permission:
    print("You can drive")
else: 
    print("You can't drive yet")


# Logical operators: 'or' and 'not'

day = "Monday"

if day == "Saturday" or day== "Sunday":
    print("It is the weekend")
else:
    print("It's the weekday")



print("--- Using 'is' and 'not' --- ")

if day is not "Monday":
    print("It's not Monday, Thankfully")



# Challenge 1: Movie Admission
# Ask the user for their age. 
# If under 13, “You can watch PG or G movies.”
# If 13–17, “You can watch PG-13 movies.”
# If 18+, “You can watch any movie.”
# Example output:
# Enter your age: 15
# You can watch PG-13 movies.


age = int(input("Enter you age: "))

if age < 13:
    print("YOu can PG or G movies ")

elif 13<= age <= 17:
    print("You can watch PG-13 movies")

else: 
    print("You can watch any movie")



# Challenge 2: Leap Year
# Rules:
#   - Years divisible by 4 are leap years...
#   - ...unless they're divisible by 100, then they're NOT leap years...
#   - ...unless they're also divisible by 400, then they ARE leap years.
# Example output:
# Enter a year: 1900
# 1900 is not a leap year.
# (Test: 2024 -> leap, 1900 -> not, 2000 -> leap)


year = int(input("Enter a year: "))

if year % 4 ==0 and year % 100 != 0:
    print(f"{year} it is a leap year ")

elif year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
