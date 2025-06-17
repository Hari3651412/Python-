def palindrome_check():
    word="madam"
    if word==word[::-1]:
        print("palindrome is present")
    else:
        print("not present")
        print("palindrome")
palindrome_check()

#with arguments

def palindrome(word):
    if word==word[::-1]:
        print("not palindrome")

palindrome("Harisandana")
p=palindrome("saisri")

#with parameters

def palindrome():
    p=input("enter a name :")
    if p==p[::-1]:
        print("palindrome")
    else:
        print("not palindrome")


palindrome()

