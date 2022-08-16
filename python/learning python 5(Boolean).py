print(10>9)
print(10==9)
print(10<9)


#printing a condition statement 
a = 200
b = 33

if b > a: 
    print ("b is greater than a")
else:
    print ("b is not greater than a")
 
 
 #bool () function is used evaluate if a value is true of false    
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15

print (bool(x))
print (bool(y))
   
   
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#honestly i don't understand what w3schools was teaching me here 
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print (bool(myobj))


#printing YES! if the functions returns true, otherwise print NO!

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print ("NO!")
    
#in boolean we can find out if an object is a certain data type, thefore if it is correct it prints true and if it is wrong well you know what's next
x= 200
print(isinstance(x,int))
    