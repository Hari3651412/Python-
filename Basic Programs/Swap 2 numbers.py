# 5. Write a program to swap two numbers using a temporary variable.
a=int(input("Enter a number "))
b=int(input("Enter a number "))
temp=a
a=b
b=temp
print("After swapping")
print(f" First value is {a} ")