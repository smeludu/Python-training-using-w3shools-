#Truple! What  is Turple?
#Turple is used to store multiple items in a single variable
#set, list and dictionary are other data types that are used to store items/data
#unlike the othes turple is unchangeable and order - meaning it can not be changed, items can not be removed or added after it is stored 
# it is written with round bracket unlike list [] and set {}

thistuple =("apple", "banana", "cherry")
print(thistuple)

#tuple also allows duplicate value 
thistuple =("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


thistuple =("apple", "banana", "cherry")
print(len(thistuple))


thistuple =("apple",)
print(type(thistuple))

thistuple =("apple") #note it is not a tuple without ,
print(type(thistuple))

#tuple can be any data type 
tuple1 =("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)


#tuple containing different data types 
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

#defined/printing the data type 
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))



#the tuple() constructor 
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-bracket 
print(thistuple)


#Accessing tuple items 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Accessing tuple items using negtive indexing 
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])# -1 starts from the last value 


#range of indexes 
thistuple = ("apple", "banana", "cherry", "orange", "melon", "mango")
print(thistuple[2:5])

#range of indexes 
thistuple = ("apple", "banana", "cherry", "orange", "melon", "mango")
print(thistuple[:4])

#range of indexes 
thistuple = ("apple", "banana", "cherry", "orange", "melon", "mango")
print(thistuple[2:])


#changing item in tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1]= "Kiwi"
x = tuple(y)
print(x)


#adding item in tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.append ("orange")
x = tuple(y)
print(x)


#another way to add items to a tuple is 
#changing item in tuple
x = ("apple", "banana", "cherry")
y =("Kiwi", )

x +=(y)
print(x)


#deleting item in tuple
x = ("apple", "banana", "cherry")
y = list(x)
y.remove ("apple")
x = tuple(y)
print(x)


#another way to delete an item in tuple
x = ("apple", "banana", "cherry")
del x
#print(x) #printing this will raise an error because the tuple no longer exist 


#unpacking from variable
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print (green)
print (yellow)
print (red) 
#note packing is already done normally while assigning variable 
#once it gets to * it because a list 
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print (green)
print (yellow)
print (red) 

#loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print (x)
    
    
thistuple = ("apple", "banana", "cherry")
for i in range (len(thistuple)):
    print (thistuple[i])
    
    
#whileloop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print (thistuple[i])
    
    i = i + 1
    
    
    
#joining tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


#multiply the tuple bye a given number 
mytuple = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)