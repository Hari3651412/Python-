name = "dsvfiuhiufghu"

fruits = ["apple", "banana", "orange",9,10,True,False,["ball",]]

"""
it supports indexing
ordered
mutable
mied data
lists can be nested
"""

"""
common methods

append(),insert(),pop(),remove(),clear(),extend(),resvere(),sort()
"""

names = ["shanmukh","anand","sudeep","suresh","ravi","kohli","kumar"]
print(names[0:3:2])
print(names[-1])
names.append("dhoni")
print(names)
names.insert(10,"rahul")
print(names)
names.extend(["kiran","maxii","kumari"]) # we can add multiple values at once
names.remove("shanmukh")
print(names)
names.pop(2)
print(names)
print(names.index("kohli"))

numbers = [1,2,3,4,5,6,7,8,9,10,2,3,2,2,2,2]
print(numbers.count(2))
numbers.sort()
print(numbers)




