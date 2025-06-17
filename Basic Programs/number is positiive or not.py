#write a program to check whether a number is positive, negative, or zero.


# Write a program to check whether a number is positive, negative, or zero.

try:
    num = float(input("Enter a number: "))  # Ensure valid numeric input
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Invalid input! Please enter a numeric value.")