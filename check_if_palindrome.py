# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

# Expected Output:

# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

#Create a function to check whether it is a palindrome
def check_if_palindrome(check_number):
#Create a condition if the number is palindrome then print the result saying it is a palindrome
    if check_number[::-1] == check_number:
        print("Orginal number is", check_number)
        print("Yes, given number is a palindrome number.")    
#If not print the result saying it is not a palindrome
    else:
        print("\nOriginal number is", check_number)
        print("No, given number is not a palindrome number.")

#Create a variables with the given numbers
check_number_1 = str(121)
check_number_2 = str(125)

#Call out the function
check_if_palindrome(check_number_1)
check_if_palindrome(check_number_2)
