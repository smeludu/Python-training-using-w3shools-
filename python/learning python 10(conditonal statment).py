a = 33
b = 200
if b > a:
 print ("b is greater than a")#note that there is an indentation, because without it there will be an error 
 
#elif is used when the previous condition were not true 
 a = 33
 b = 33
 if b > a:
     print ("b is greater than a")
 elif a == b:
     print ("a and b are equal")
     
     
#else is used incase something is used in the previous condition. Pretty much giving it another condition 
 a = 200
 b = 33
 if b > a:
     print ("b is greater than a")
 elif a == b:
     print ("a and b are equal")
     
 else:
     print ("a is greater than b")


a = 200
b = 33
if b > a:
     print ("b is greater than a")
else:
     print ("b is not greater than a")


#short hand if 
if a > b: print("a is greater than b")


#short hand if else 
a = 2
b = 330
print ("A") if a > b else print ("B")

#note in a short hand you can have multiple if and else statement, and this is called ternary operations or conditional expressions 
a = 330
b = 330
print ("A") if a > b else print ("=") if a == b else print ("B")


#and keyword is used to add/join conditional statement together 
a = 200
b = 33
c = 500
if a > b and c > a:
    print ("Both conditions are True")
    
#or is similar to and but it has a different meaning
a = 200
b = 33
c = 500
if a > b or a > c:
    print ("At least one of the condition is True")

#Nested if 
x = 41 
if x > 10:
    print ("Above 10, ")
    if x > 20:
        print ("and also above 20!")
    else:
        print ("but not above 20.")
        
#pass is used when if statement is not going to print anything and you don't want it to print an error message
a = 33
b = 200
if b > a:
    pass #noting will pass because there is no print statement
 
    