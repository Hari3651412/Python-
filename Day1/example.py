colors=("red", "green", "blue", "yellow")
print(colors)

second_item=colors[1]
print(second_item)

last_elements=colors[-2:]
print(last_elements)

single_item=("python",)
print(type(single_item))



numbers=(1,2,3)
a,b,c=numbers
print(a,b,c)

t=(4,5,6,5,7)
t1=t.count(5)
print(t1)

t=(4, 5, 6, 5, 7)
t2=t.index(6)
print(t2)



mylist=[1, 2, 3, 4]
mytuple=tuple(mylist)
print(mytuple)
print(type(mytuple))

t1=(1,2)
t2=(3,4)
t3=t1+t2
print(t3)

tuple=(9,8)
repeat_tuple=tuple*3
print(repeat_tuple)