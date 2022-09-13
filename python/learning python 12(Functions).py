from re import X


def myfunction ():
 print ("Hello from a function")
 
 
myfunction()#creating function and calling the function 



def my_function(fname):
    print (fname + "Refsnes")
    
my_function("Emil")
my_function("Tobias")
my_function("Linus")


# A function is a block of code that only runs when called, and you can pass data known as parameters.
#when function expects two argument it gets two argument or you get an error message

def my_function (fname, lname):
    print (fname + " " + lname)
    
    
my_function ("Emil","Refsnes")


#if you do not know how many arguments will be passed use * this way the function will recieve tuple arguments
#it must be added before the paramters name in the function 


def my_function (*kids):
    print ("The youngest child is " + kids[2])
    
    
my_function ("Emil", "Tobias","Linus")

#sending arguments with key = value syntax 
# note if the amount of keyword is unknown use **
def my_function (child3, child2, child1):
    print ("The youngesr child is" + child3)

my_function(child1 = "Emil", child2= "Tobias", child3 = "Linus")


#using a default parameter
#when the function is called without a parameter it uses the default parameter 
def my_function (country = "Norway"):
    print ("I am from " + country)

my_function ("Sweden")
my_function ("India")
my_function ()
my_function ("Brazil")

#passing a list as an argument
def my_function(food):
    for x in food:
        print (x)
        
fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#returning values
def my_function(x):
    return 5 * x

print (my_function(3))
print (my_function(5))
print (my_function(9))


#pass statment 
def my_function():
    pass

#recursion statement 
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else: 
        result = 0
    return result 
print ("\n\nRecursion Example Results")
tri_recursion(6)