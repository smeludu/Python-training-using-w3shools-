X = str(3) #x will be '3'
y = int(3) # y will be 3.0
z = float(3) # z will be 3.0
print (X)
print (y)
print (z)

x = 5 
y = "John"
print(type(x))
print(type(y))

# in case sensitive A does not override a
a = 4 
A = "sally"
print(a)
print(A)

# variable names must start with an underscore charater or a letter 
# can not start with a number 
# can only contin alpha numeric charaters
# final they are case sensitive 


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print (myvar)
print (my_var)
print (_my_var)
print (myVar)
print (MYVAR)
print (myvar2)

# Assigning multiple variables 
X,Y,Z = "Orange", "Banana", "Cherry"
print(X)
print(Y)
print(Z)


# Y and Z will override the previous value 
#one value equal to so many variables 
X=Y=Z = "Orange"
print (X)
print(Y)
print(Z)

#Unpacking a collection 
fruits = ["apple", "banana", "cherry"]
X, Y, Z = fruits 
print(X)
print(Y)
print(Z)

# output Variables 
X = "Python is awesome"
print (X)

X = "Python"
Y = "is"
Z = "awesome"
print(X, Y, Z)

X = "Python"
Y = "is"
Z = "awesome"
print(X + Y + Z)

X = 5
y = 10
print (X + y)

#error occurs when you add an integer an a varibale together 
X = 5
y = "Sam"
#print (X + y)
#corrected method 
X = 5
y = "Sam"
print (X, y)


