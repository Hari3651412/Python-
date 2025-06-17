
# Construtcor
# class Person:
#     def __init__(self):
#         self.x = 10
#
# p = Person()
# print(p.x)

class Animal: #class is blue print
       def __init__(self): #initalization method
           self.x=10
p=Animal()  #object creation
print(p.x)
  #1) Default Constructor
class Person:
    def __init__(self):   #defining methods
        self.a=10
        self.b="unknown"
        self.age=10
obj=Person()        #object creation
print(obj.a)
print(obj.age)
print(obj.b)

# Parametrized constructor

class Student:
     def __init__(self,Name,Age):
         self.Name=Name
         self.Age=Age
obj=Student("Hari","20")
print(obj.Name)
print(obj.Age)

#Default ARguments


class Dog:
    def __init__(self,Bread="female",Type="puppy"):
        self.Bread=Bread
        self.Type=Type
obj=Dog()
obj2=Dog("black","male")
print(obj.Bread,obj.Type)
print(obj2.Bread,obj2.Type)

#using new ()
