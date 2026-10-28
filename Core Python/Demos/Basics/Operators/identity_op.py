x = 10 ##inmutable
y = 10 ##reuse
li1 = [10,20] ##Mutable
#can't reuse
li2 = [10,20] 

#1. is 
print(x is y)
print(id(x))
print(id(y))
print(li1 is li2)
print(id(li1))
print(id(li2))