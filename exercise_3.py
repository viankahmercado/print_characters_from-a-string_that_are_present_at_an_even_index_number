# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 3: 
# Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

#input a word and assign as variable
any_word = input("Please input a word: ")
print("Original String is:", any_word)

#loop for even characters
print("\nPrinting only even index chars:")
for i in range(len(any_word)):
    if i % 2 == 0:
        print(any_word[i])