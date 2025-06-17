class Dog:
    def Speak(self):
        return  "I make sound"
class Animal(Dog):
    def bark(self):
        return "i make noise"
obj=Animal()
print(obj.bark())
print(obj.Speak())
