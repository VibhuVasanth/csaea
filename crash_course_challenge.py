#1.Tip calculator challenge 
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

odd = 4287 % 2 

even = 4287 & 2 

if odd == 1:
    print("Park on the West side ")
elif even == 0:
    print("Park on the east side")

print("MOVING ONTO NEXT CHALLENGE")

#5. Name Tag Generator 
first = "Vibhu"
last = "Vasanth "
school = "CSAEA "

print(f"Hello my name is  {first}  {last} from { school}" )

print("MOVING ONTO NEXT CHALLENGE")

#6. Grocery List Manager

groceries = ["Milk", "Eggs", "Bread"]

groceries. insert (0 , "cheese")

print(len(groceries))
print(groceries)