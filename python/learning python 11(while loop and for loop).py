#WHILE LOOP
i = 1
while i < 6:
 print (i)
 i+=1 
 
 
#break statment 
i = 1
while i < 6:
 print (i)
 if i == 3:
  break 
 i += 1
 
 
 
#continue statment 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print (i)
    
    
#else statement 
i = 1
while i < 6:
 print (i)
 i+=1 
else:
    print ("i is no longer less than 6")
    
    
#FOR LOOP
fruits = ["apple", "banana", "cherry"] #looping through strings 
for x in fruits:
    print (x)
    
#break statemnt   
fruits = ["apple", "banana", "cherry"] #looping through strings 
for x in fruits:
    print (x)
    if x == "banana":
     break #this prints apple first 


fruits = ["apple", "banana", "cherry"] #looping through strings 
for x in fruits:
    if x == "banana":
     break
    print (x) #this does not print apple first


#the continue statment 
fruits = ["apple", "banana", "cherry"] #looping through strings 
for x in fruits:
    if x == "banana":
     continue
    print (x) #this does not print apple first  
    
#range loop function
for x in range (6):
    print (x)

for x in range (2,6):
    print (x)
    
for x in range (2, 30, 3): #in increment of 3 
    print (x)
    
    
#else in for loop 
for x in range (6):
    print (x)
else:
    print ("Finally finished!")
    
#adding a break statment to for with else but NOTE that else block will not be executed
#else in for loop 
for x in range (6):
    if x == 3: break 
    print (x)
else:
    print ("Finally finished!")


#nested loops 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print (x, y)
        
        
        
#pass statment 
#else in for loop 
for x in [0, 1, 2]:
    pass
