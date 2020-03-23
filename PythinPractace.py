def main():
    print("finnaly we are pythoning")

if __name__ == "__main__":
    main()
# 1. Write a program that takes a name as user input and prints
# "Hello name".

name = "Teo"

print("Hello {}!".format(name))



# 2. Create a variable called x and set it to 10. Print x to the
# console.

x = 10

print(x)

# 3. Write a program that takes a number and tells the user if the
# number is greater than 10, less than 10, or equal to 10. Don't
# forget to convert the string into an integer.
def lessorgreater(number):

    if number > 10:
        print("{} is greater than 10".format(number))
    if number < 10:
        print("{} is less than 10".format(number))
    if number == 10:
        print("{} is equal to 10".format(number))

lessorgreater(69)




# 4. Write a program that takes a number as a user input and tells
# the user if it is even or odd.
# 5. Create a list and write a program that prints each individual
# element to the console.
# 6. Write a program that uses a loop fill an empty list with 10
# numbers and prints the list to the console. The numbers can
# be random or simply put in the numbers 0-9 or 1-10 in
# ascending order.
# 7. Write a program that takes a number as user input and tells
# you how many numbers in a list are less than the number that
# the user gave.
# 8. Write a program that keeps asking the user to enter a word.
# For each word that the user enters, the program prints out
# each letter in the word on a new line. When the user enters
# “s 