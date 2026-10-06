import math 
#.Tip calculator challenge 
bill = 50 
tip = 20/100 *  50 

total = tip + bill 

print(f"Tip: {tip} total: {total}")

print("MOVING ONTO NEXT CHALLENGE")


#2. Temprature Converter
fahrenhiet = 212

c = (fahrenhiet - 32)*5 /9

print (f"212 F is {c}")

print("MOVING ONTO NEXT CHALLENGE")


#3. Logic screen 
password = "csaea2026"
attempt  = "CSAEA2026"

if attempt != password:
    print("Access denied ")
else:
    print("Access Granted ")

print("MOVING ONTO NEXT CHALLENGE")

#4. Even and Odd Parking 
plate = 4827





if plate % 2 == 0:
    print("Park on the east side")
else:
    print("Park on the west side")

print("MOVING ONTO NEXT CHALLENGE")

#5. Name Tag Generator 
first = "Ada"
last = "lovelace "
school = "CSAEA "

print(f"Hello my name is  {first}  {last} from { school}")

print("MOVING ONTO NEXT CHALLENGE")

#6. Grocery List Manager

groceries = ["Milk", "Eggs", "Bread"]

groceries. insert (0 , "cheese")


print(len(groceries))
print(groceries)

print("MOVING ONTO NEXT CHALLENGE")

#7.Times Table Helper 

number = 7 
i = 1 
for i in range(1, 11):
    new_number = number * i 
    print(f"{number}*{i} = {new_number}")



print("MOVING ONTO NEXT CHALLENGE")


# Roller Coaster gate 8

height = 50
age = 8
has_adult = True
count = 0

if height >= 48 and age  > 10 :
    print("you may ride")

elif has_adult == True :
    print(" you may ride ")

else: 
    print("you may not ride ")
# 9 Report card 
score = 84
 
if score  >= 90:

    print("A")
elif score >= 80:
    print("B")

elif score >= 70:

    print("c")
else:
    print("D")

# 10. shopping cart 

cart = [12, 5, 30, 8]
print(f"Items: {len(cart)}")
total  = 0 
for x in cart: 
     total= total + x 
print(f"${total}" )


#11 Pizza ordering 
students = 23
slices_per_student = 2
slices_per_pizza = 8

pizza = students * slices_per_student
x = math. ceil(pizza / 8 )

print(f"Order {x} pizzas")

number_of_totalslices = x * 8


print(f"Extra Slices:{number_of_totalslices % students}")

#Rocket launch 
import time
start = 10

for x in range(start, 1, -1):
    print(x)
    time.sleep(1)
    
print("liftoff")

#Saving goal 
savings = 0
weekly_deposit = 15
goal = 100
 
weeks = 0 
while savings  <= goal:
    savings += weekly_deposit
    weeks += 1
print(f"Weeks:{weeks}")
print(f"Saved: {savings}")

#High Score 
scores = [340, 1250, 980, 1510, 720]

y = scores[0]
index = 0
while index < len(scores):
    if scores[index] >y: 
        y = scores[index]
    index = index+1 

print(f"High score: {y}")


#Garden Fence 


area = 49

one_side = math.sqrt(area)

fencing_needed = one_side * 4


print(f"Fencing Needed {float(fencing_needed)} ft")


#Parking meter 

minutes_parked = 50
block_length = 15
cost_per_block = 1
 
cost = minutes_parked / block_length

cost = math.ceil(cost)

print((f"You owe ${cost}"))


#Playlist Swap 


playlist = ["Intro", "Song A", "Song B", "Finale"]

playlist[0] = "Finale"

playlist[-1] = "Intro "

print(playlist )


#Leap Year Checker
year = 1900

if year % 4 ==0 and year % 100 != 0:
    print(f"{year} it is a leap year ")

elif year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Speed trap 
speed_limit = 55
speed = 71

fine = speed - speed_limit

#Drivers 1 to 10 mph over the limit get a warning, 11 to 20 over pay $100, and more than 20 over pay $250. Print the result for this driver. Use math operators and conditionals (if, elif, else).

if 1 <= fine <= 10:
    print("Warning")
elif 11 <= fine <= 20: 
    print("Fine $100")
else: 
    print("Fine $250 ")



#Class Pass rate #didn't finish I couldn't  understand it 

# grades = [88, 65, 72, 91, 54, 70]
# passing = 70

# i = 0 
 
# for x in grades: 
#     if grades >= 70:
#         i = i + 1
# else: 
#     i = 0 

# print(i)        














        



