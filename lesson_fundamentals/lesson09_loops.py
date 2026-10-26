# # LOOPS IN PYTHON
# # Loops repeat a block of code until they hit a limit or condition.
# # They exist to save us from typing the same line 500 times.
# # Python gives us for-loops and while-loops.


# import time

# # The FOR-LOOP.
# # A for-loop repeats for each element in a sequence (like a list or string).

# animals = ["Chicken", "Lamb", "Snake", "Goose","donkey", "cow","Fish"]

# print("\nOur Animals: ", animals)

# for animal in animals:
#     print("Now I'm petting a",animal )

#     time.sleep(0.5)# pause for a full second


# # We can loop a specfic number of times using range().


# for i in range(5):
#     print("\nCounting:", i)

#     time.sleep(0.5)


# # range(start, stop, step)

# for num in range(5, 100,5):
#     print("The skipping numbers are", num)


# # Strings are also iterable, so they be looped as well!

# fav_word = "Shennanigans"

# letter_list = []
# for letter in fav_word:
#     print(letter)
#     letter_list.append(letter + "!")

# print(letter_list)


# # Challenge 1: Sum Calculator
# # Use a for-loop to find the sum of numbers from 1 to 10.
# # ie, 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# # Expected output: 55
# print()
# total = 0 

# for i in range(1, 11):
#     total += i
# print(total)


# # A while-loop repeats *while* a condition is true.
# # If you forget to change the condition, it loops forever.
# # And then your program becomes immortal. Avoid that.

# # += to add to a variable, -= to subtract to a variable, = to overright

# count = 0


# while count < 5:
#     print(f"Looping' -- We are on loop index # {count}")
#     count += 1
#     time.sleep(0.5)

# #Example with user input

# user_input = ""
# while user_input != "exit":
#     user_input = input("type 'exit to escape ")

# #loop control statements

# for i in range(1, 11):
#     if i == 3:
#         print("Skipping 3")
#         continue
#     if i == 6:
#         print("Breaking at 6")
#         break #stop the loop entierly
#     if i == 9:
#         pass #place holder.does nothing. will code in the future

#     print("Number", i)


# Challenge 2: Guess Until Correct
# Create a while-loop that keeps asking for a number until the user types 7.


user = ()
while user != 7:
    user = int(input("Input a number: "))
    if user == 7:
        print("You got it!!!")
