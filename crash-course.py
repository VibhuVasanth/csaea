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