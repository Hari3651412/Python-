from dataclasses import replace

fruits=["apple", "banana", "cherry", "date", "elderberry"]
fruits.append("fig")
print(fruits)
fruits.insert(2,"blueberry")
print(fruits)
fruits.remove("date")
print(fruits)

fruits.pop(-1)
print(fruits)

print(fruits[:3])
print(fruits[1:4:2])
print(fruits[::-1])
print(fruits)

print(fruits.index("banana"))
print(fruits.count("apple"))

fruits.sort()
print(fruits)


String = "PythonProgramming"
Substring=String[0:6]+" Language "
print(Substring)
print(String.upper())
print(String.lower())

Substring=String[6:17]
print(Substring)

Text=String+" is fun! "
print(Text)

String = "PythonProgramming"
if "thon" in String:
 print("thon is present")
else:
   print("thon is not present")

String = "PythonProgramming"
Substring=String.replace("programming","Lanuage")
print(Substring)

index=String.find("g")
print(index)
String="Python Programming"
words=String.split(   )
print(words)

String= "Python Programming"
clean_string = String.strip()  # Removes leading and trailing spaces
print(clean_string)

String= "PythonProgramming"
count_m=String.count("m")
print(count_m)