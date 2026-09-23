import math
#when you import any libraries it is always the first few lines of code 

#comment


# here 
# is 
# a 
# comment 
#to make lines of words that are not code, just highlight, then press control and the press forward slash

print("Hello World!")

#Variable Declarations:

a = 4 # This is a integer 
b = 5.5 # This is a float 
c = "CSAEA" # This is a string 
d = False # This is a boolean(VERY IMPORTANT NAMES AFER GEORGE BOOL)


#These 4 data types you will need for the AP EXAM(VERY IMPORTANT!!!!!!)

print(a)
print(b)
print(c)
print(d)

#or you can do 

print(a,b,c,d)

#operators
# These include, +,-,/,* and then you know modulus %, ** exponent, //

#compound operators
#+=, -=, /=

e = 10 % 5

print(e)

e += 7

print(e)

# f - string- creates a dynamic string, mixes diffrent data types into a one sentence or string also known as formatted strings 

print(f"e is equal to {e} ")

e -= 7

e+=12 

print(f"e is NOW equal to {e}")



# COMPARISONS (boolean, which always returns TRUE or FALSE)

#  <   >    <=   >=    ==    !=

print(4<5)
print(7 ==4)
print(1!= 2)

isEqual = 5 == 6

print(isEqual)

isEqual = 5 == 5

print(isEqual)


isequal = "YES" == "YES"
print(isequal)

#remeber no matter what the casing counts, it whether it is upper case or lower case matters a lot 


#Logical Operators 
#Has what is called ORDER OF PRECEDENCE: the three words you need to know is {not   and     or }

f = False 
t = True
print(not f )#True

print (t and f)#True 

print (f and t ) #False

print(f or t ) #True

print(f or t and not f )#you have to follow the order of precedence{this will be true}

#when you are using not, it will always be the opposite of what the boolean value is 
# if you are doing the and operator for example false and true it will return false, and true and true will reture true so you have to have the same thing like t and t for it return t and same for false you know what I mean

#Next Topic [CASTING]
# to change it you would do like int() or same fro string like when you do it with the inputs
g = int(5.9)
z = str(5.5)
print(type(z))
print(g)
print(z)

#TOPIC - [STRINGS]

s1 = "Goodnight "

s2 = "and "

s3 = "Goodbye "

end = s1 + s2 + s3

end += ", Cowboy."

print(end + "\n")

#"\n means your adding a new line at the end of the printed sentence, remeber the syntax and you used this to make your statments to look nice "


#Libraries - you pretty much know this just make sure that you understand and just continue to take notes although you already know most of these

#Math Library 
#Functions within these libraries include 
# max, min, square root, 
#dot operator when you are calling any libraries 

print(math.sqrt(14))
print(math.ceil(3.65))#ceil is to round up
print(math.floor(8.94))#floor is round down
print(math.pow(2, 4))#it shows the  exponent 2 to the power of 4 


#Conditionals for example if something happens this happens


#These include, if , elif(else if ), else 

t = True
f = False

if f:
    print("You reached the first condition ")
else:
    print("Reached else")



if 1 != 2:
    print("You reached the first condition ")
else:
    print("Reached else")


if 1 == 2:
    print("You reached the first condition ")
else:
    print("Reached else")


if f: #it runs the final block because the first two blocks of code are not true so it returns the final block
    print("You reached the first condition ")

elif t:
    print("Reached second condition")
else:
    print("Reached else")


if 1 > 1 and 1 == 1:
    print("You reached the first condition ")
elif 9 != 9 or 3 !=3 :
    print("Reached second condition")
elif 10 != 10:
    print("Reached third condition")
else:
    print("Reached else")

#Lists 
# A list can hold any type, and can grow or shrink at any time.
# to make a list you use brackets python automatically recognonizes it 
#to count what is within your lists you use what is called a index.
# for example 34 would b index 0, and so on and so forth as you count up. 

nums = [34,52,3,8,64]

print(nums)

# To print a specfic value/item within the list you would print just like below 

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

#you can use negative numbers to index the numebr and pull in a backwards order
print(nums[-1])
print(nums[-2])
print(nums[-3])

#to pull out numbers and perform  a function you would do it like the way the you did it below

print(nums[1] + nums[4])

#to change or to do something within a list you would do it like this

nums[0] = 13
nums[1] = 24
nums[2] = 15
nums[4] = 2012

print(nums)

#list methods these are special built in methods
#you use a special dot operator . append mean to add something to the end of it  and same for remove words.remove or words.append
words = []

words.append("Vibhu")
words.append("Ritika")
words.append("Priya")
words.append("Vasanth")
words.append("Hi")

print(words)
words.remove("Hi")
words.insert(0, "Our Family ")
#There is a special function called length which prints the number of items within your list 
length = len(words)

print(words)

print(length)



# Loops/ iteration 
# A for loop will iterate over a RANGE
## A range (Stop), range (start, stop), range(start, stop, step)
# it goes through each item in your conditions 



for i in range(5):
    print(i)

animals = ["Sheep", "Deer", "Moose"]
print(f"List: {animals}")

for a in animals :
    print(f"We saw a {a}")


nums = [5.1 , 2.2, 5.3, 3.4, 8.5]

# print each value in list nums

# for n in nums :
    # print(n)
    

for i in range(len(nums)):
    print(nums[i])

#debugging- is when you understand the code or see why it is not working

print(len(nums))



# A while a loop, this runs until the condition is true 
# when the codition becomes false, it stops

x = 5

x < 10 

while x < 10:
    print(x)
    x +=1


t = True 
F = False

# while t or F:
    # print("hi")
